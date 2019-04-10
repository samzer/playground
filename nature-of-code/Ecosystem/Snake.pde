class Snake extends Mover {
  float topspeed;
  PImage snake;

  Snake() {
    // Start in the center
    //position = new PVector(width/2,height/2);
    position = new PVector(random(0,width),random(0,height));

    velocity = new PVector(0,0);
    topspeed = 5;
    snake = loadImage("img/Snake.png");
    mass = 100;
    acceleration = PVector.random2D();

  }

  void update() {
    // Velocity changes according to acceleration
    PVector acc = PVector.random2D();
    acceleration.add(acc);
    
    acceleration.mult(0.2);
    velocity.add(acceleration);

    // Limit the velocity by topspeed
    velocity.limit(topspeed);
    position.add(velocity);
    acceleration.mult(0);
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
  
  void applyForce(PVector force) {
    PVector f = PVector.div(force, mass);
    acceleration.add(f);
  }
  
  PVector repel(Mover m) {
    PVector force = PVector.sub(position,m.position);
    float distance = force.mag();
    distance = constrain(distance,5.0,400.0);


    force.normalize();
    float strength = (- 4 * mass * m.mass) / (distance * distance);
    force.mult(strength);
    return force;
  }
}
