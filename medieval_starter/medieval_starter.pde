final int W=64, H=64;         //tile width and height
PImage bk, player, platform1, platform2,house ,flag, banner, door, tree;

void setup(){
  size(512,512);
  bk = loadImage("background_0.png");      // 512 x 512
  player = loadImage("player_0.png");      // 64 x 64
  platform1 = loadImage("platform_13.png");// 64 x 64
  platform2 = loadImage("platform_14.png");// 64 x 64
  house = loadImage("house.png");
 flag = loadImage("flag.png");
 banner = loadImage("banner.png");
 door = loadImage("door.png");
 tree = loadImage("treeLong.png");
}

void draw(){
  // set the background to background_0.png
  background(bk);
  // draw the player image at (mouseX, 6*H) - i.e. your player should move with mouseX 

  // draw the platform at y = 7 * H
  imageMode(CORNERS);
   image(flag,55,0); 
   image(house,18,40);
  image(platform1,0,7*H);
    image(platform1,3*H,7*H);
        image(platform1,H,7*H);
        image(platform1,2*H,7*H);
        image(platform2,5*H,7*H);
        image(platform1,4*H,7*H);
        image(banner,55,170);
        image(door,55,380);
        image(tree,205,365);
  image(player,mouseX,6*H);
}
