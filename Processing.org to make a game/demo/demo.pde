// 1. code to show functions and how RGB colors work

//size(640, 320);

//background(255, 255, 0);

//stroke(255, 0, 0);
//line(350, 150, 200, 250);

//stroke(0, 0, 255);
//fill(0, 255, 0);
//ellipse(100, 100, 100, 100);

//stroke(0); // assumes same value for all three parameters
//fill(255, 0, 0);
//rect(450, 100, 100, 200);
//fill(0, 200); // transparency
//rect(400, 200, 100, 100);

// 2. refined flow with setup and draw

//void setup() {
//  size(640, 320);
//}

//void draw() {
//  stroke(0);
//  fill(255, 0, 0);
//  rectMode(CENTER);
//  rect(470, 80, 100, 100);
//  fill(0, 200);
//  rect(400, 200, 50, 100);
//}

// 3. demonstrating mouseX and mouseY

//void setup() {
//  size(640, 320);
//}

//void draw() {
//  background(50); //what happens when move this line to the setup function?
//  stroke(0);
//  rectMode(CENTER);
//  fill(255, 0, 0, 200);
//  rect(mouseX, mouseY, 70, 70);  //change parameter to say (height-mouseX)
//}

// 4. doodling by keeping the background in setup

//void setup() {
//  size(640, 320);
//  background(50);
//}

//void draw() {
//  //background(50);
//  stroke(255);
//  strokeWeight(mouseX/15);
//  line(pmouseX, pmouseY, mouseX, mouseY);
//}

//void mousePressed() {
//  background(50);
//}

// 5. intro to variables and random

//int x;  //declaration
//float y;

//void setup() {
//  size(640, 320);
//  x = int(random(0,10));    //initialization
//  y = random(height);
//}

//void draw() {
//  background(50);
//  fill(255);
//  ellipse(x,y,25,25);
//  x = x + 2;    //usage
//}

// 6. conditionals

float x,y,speed_x;

void setup() {
  size(640, 320);
  x = 0;
  y = random(height);
  speed_x = 6.0;
}

void draw() {
  background(50);
  fill(255);
  ellipse(x,y,25,25);
  x = x + speed_x;
  if(x > width+1 || x < 0){    //when circle reaches either edge, change direction
    //speed_x = -1*speed_x;       //simply just reverses direction
    speed_x = -1.5*speed_x;    //increases speed each time by 50%
  }
}
