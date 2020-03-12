import urllib.error, urllib.request, urllib.parse
import json
target = 'http://py4e-data.dr-chuck.net/json?'  #使用这个接口，需要 key参数且值为42
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})
#对字符串进行url编码，直接传递参数和值构成的字典
print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
# print(json.dumps(js, indent = 4)) #查看接收到的文件结构
print('Place id', js['results'][0]['place_id'])
