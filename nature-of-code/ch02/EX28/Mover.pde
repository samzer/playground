// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

class Mover {

  PVector position;
  PVector velocity;
  PVector acceleration;
  float mass;
  float R,G,B;

  Mover(float m, float x, float y) {
    mass = m;
    position = new PVector(x, y);
    velocity = new PVector(1, 0);
    acceleration = new PVector(0, 0);
    R = random(0,255);
    G = random(0,255);
    B = random(0,255);
  }

  void applyForce(PVector force) {
    PVector f = PVector.div(force, mass);
    acceleration.add(f);
  }

  void update() {
    velocity.add(acceleration);
    position.add(velocity);
    acceleration.mult(0);
  }

  void display() {
    //stroke(0);
    //strokeWeight(2);
    colorMode(RGB, 100);
    fill(R,G,B, random(0,255));
    noStroke();

    ellipse(position.x, position.y, mass*25, mass*25);
  }
}
