# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = [10,5,1]
    i = 0
    j = 0
    while(money > 0):
        if coins[i] > money:
            i += 1
        else:
            j += 1
            money -= coins[i]
    return j




if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
