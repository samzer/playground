class Fly {

  // The Mover tracks position, velocity, and acceleration
  PVector position;
  PVector restPosition;
  PVector velocity;
  PVector acceleration;
  // The Mover's maximum speed
  float topspeed;
  PImage fly;
  float tx,ty;
  float x,y;

  Fly() {
    // Start in the center
    position = new PVector(width/2,height/2);

    //restPosition = position.get();
    velocity = new PVector(0,0);
    topspeed = 4;
    //acceleration = PVector.random2D();
    //acceleration.mult(2);
    fly = loadImage("img/fly.png");
    tx = random(0,10000);
    ty = random(0,10000);
  }

  void update() {
    x = map(noise(tx), 0, 1, -3, 3);
    y = map(noise(ty), 0, 1, -3, 3);

    acceleration = new PVector(x, y);
    //acceleration.mult(0.2);
        //acceleration.mult(random(2));

    velocity.add(acceleration);

    // Limit the velocity by topspeed
    velocity.limit(topspeed);
    position.add(velocity);
        tx += 0.01;
    ty += 0.01;
  }

  void display() {
    stroke(0);
    strokeWeight(2);
    fill(127,200);
    pushMatrix();
    imageMode(CENTER);
    translate(position.x,position.y);
    rotate(velocity.heading() + PI/2);
    image(fly, 0,0,38,38);
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
