class Snake {

  // The Mover tracks position, velocity, and acceleration
  PVector position;
  PVector restPosition;
  PVector velocity;
  PVector acceleration;
  // The Mover's maximum speed
  float topspeed;
  PImage snake;

  Snake() {
    // Start in the center
    position = new PVector(width/2,height/2);

    //restPosition = position.get();
    velocity = new PVector(0,0);
    topspeed = 2;
    //acceleration = PVector.random2D();
    //acceleration.mult(2);
    snake = loadImage("img/Snake.png");
  }

  void update() {
    // Velocity changes according to acceleration
    acceleration = PVector.random2D();
    acceleration.mult(0.2);
    velocity.add(acceleration);

    // Limit the velocity by topspeed
    velocity.limit(topspeed);
    position.add(velocity);
  }

  void display() {
    stroke(0);
    strokeWeight(2);
    fill(127,200);
    pushMatrix();
    imageMode(CENTER);
    translate(position.x,position.y);
    rotate(velocity.heading() + PI/2);
    image(snake, 0,0,68,68);
    popMatrix();
  }

  void checkEdges() {

    //[full] When it reaches one edge, set position to the other.
    if (position.x > width) {
      position.x = 0;
    } else if (position.x < 0) {
      position.x = width;
    }

    if (position.y > height) {
      position.y = 0;
    } else if (position.y < 0) {
      position.y = height;
    }
  }

  void draw() {
     update();
     checkEdges();
     display();
  }
}
