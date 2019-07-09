
class Mover {
  PVector position;
  PVector velocity;
  PVector acceleration;
  float mass;
  int degree;

  Mover() {
    position = new PVector(0,0);
    velocity = new PVector(0,0);
    acceleration = new PVector(0,0);
    degree = 0;
  }
  
  void update() {
    //velocity.add(acceleration);
    //position.add(velocity);
    //acceleration.mult(0);
    degree += 4;
  }

  void display() {
    stroke(0);
    strokeWeight(2);
    fill(0);
    translate(width/2, height/2);
    rotate(radians(degree));
    
    rectMode(CENTER);
    rect(position.x,position.y,4,80);
    ellipseMode(CENTER);
    ellipse(position.x,position.y - 40, 20, 20);
    ellipse(position.x,position.y + 40, 20, 20); 

  }
}
