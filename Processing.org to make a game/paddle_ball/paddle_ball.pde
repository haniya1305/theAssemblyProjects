float Xb, Yb, r, speedX, speedY;    // ball x-y location, size (radius), and speed for each component
float Xp, Yp, w, h;                 // paddle x-y location, width and height 

boolean isGameOver = false;         // boolean expression used to end the game  
int score = 0;                      // variable used to keep track of score

void setup() {
  size(400, 400);

  // initialize ball attributes
  Xb = random(r, width-r);      
  Yb = 30;                         
  r = 15;
  speedX = int(random(2, 4));   
  speedY = int(random(2, 4));

  // initialize paddle attributes
  w = 30; 
  h = 8;
  Xp = width/2;  
  Yp = height - h;

  // hide mouse cursor
  noCursor();
}

void draw() {  
  background(0);                  // we don't want the window to show the previous positions of the ball

  if (!isGameOver) {              // let it play as long as boolean expression is true

    // Draw game elements
    // draw Ball
    fill(255);   
    noStroke();
    ellipse(Xb, Yb, 2*r, 2*r);
    // draw paddle
    stroke(0, 255, 0);  
    strokeCap(ROUND);  
    strokeWeight(h);
    line(Xp-w, Yp, Xp+w, Yp);
    // draw score
    fill(255, 0, 0); 
    textAlign(LEFT);  
    textSize(16);
    text("Score: " + score, 5, 15);

    // Move game elements
    // move Paddle
    Xp = mouseX;
    // move ball 
    Xb += speedX;
    Yb += speedY;

    // check for collisions
    // bounce the ball off the two sides and the top edge       
    if (Xb >= width - r || Xb <= 0 + r)
      speedX = -speedX;
    if (Yb <= 0 + r)
      speedY = -speedY;

    // check if ball lands on the paddle
    // if the ball is at the bottom edge                          
    //     if ball lands on paddle 
    //         increment score, bounce ball up, and increase speed by 10%         
    //     else                                                                    
    //         set isGameOver to true;                                       
    float d = dist(Xp, Yp, Xb, Yb);
    if (Yb > 370 && d<(w+r)) {
      score++;
      speedY = -speedY;
      speedY = 1.2*speedY;
    } else {
      if(Yb>400)
        isGameOver=true;
    }
  }
  else { // if game over
  // putting the GameOver message and stoping the animation loop 
  background(0);
  noStroke();
  fill(255, 0, 0);
  rect(50, 100, 300, 200);
  fill(255, 255, 0);
  textSize(30);
  textAlign(CENTER);
  text("Game Over! ", 200, 190);
  text("Your score is "+score, 200, 230);
}
}
