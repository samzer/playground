// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

class Mover {

  PVector position;
  PVector velocity;
  PVector acceleration;
  float mass;

  Mover(float m, float x , float y) {
    mass = m;
    position = new PVector(x,y);
    velocity = new PVector(0,0);
    acceleration = new PVector(0,0);
  }
  
  void applyForce(PVector force) {
    PVector f = PVector.div(force,mass);
    acceleration.add(f);
  }
  
  void update() {
    velocity.add(acceleration);
    position.add(velocity);
    acceleration.mult(0);
  }

  void display() {
    stroke(0);
    strokeWeight(2);
    fill(0,127);
    ellipse(position.x,position.y,mass*16,mass*16);
  }

  void checkEdges() {
    PVector leftForce = new PVector(-1* 1/(1 + exp(width - position.x)), 0);
    PVector RightForce = new PVector(1/(1 + exp(position.x - 0)), 0);

    leftForce.mult(2);
    leftForce.mult(2);
    
    applyForce(leftForce);
    applyForce(RightForce);

    if (position.y > height) {
      velocity.y *= -1;
      position.y = height;
    }

  }

}
