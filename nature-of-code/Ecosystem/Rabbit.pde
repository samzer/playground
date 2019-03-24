class Rabbit {

  // The Mover tracks position, velocity, and acceleration
  PVector position;
  PVector restPosition;
  PVector velocity;
  PVector acceleration;
  // The Mover's maximum speed
  float topspeed;
  PImage bunny;

  Rabbit() {
    // Start in the center
    position = new PVector(width/2,height/2);

    restPosition = position.get();
    velocity = new PVector(0,0);
    topspeed = 5;
    acceleration = PVector.random2D();
    acceleration.mult(3);
    bunny = loadImage("img/bunny.jpg");
  }

  void update() {
    // Velocity changes according to acceleration
    velocity.add(acceleration);

    // Limit the velocity by topspeed
    velocity.limit(topspeed);

    if(PVector.dist(position, restPosition) > 100){
      restPosition = position.get();
      acceleration = PVector.random2D();
      acceleration.mult(0.2);
      velocity = new PVector(0,0);
    }

    if(velocity.mag() > 4){
          position.add(velocity);
    }
  }

  void display() {
    stroke(0);
    strokeWeight(2);
    fill(127,200);
    pushMatrix();
    imageMode(CENTER);
    translate(position.x,position.y);
    rotate(velocity.heading() + PI/2);
    image(bunny, 0,0,48,48);
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
