class Ballon {

  // The Mover tracks position, velocity, and acceleration 
  PVector position;
  PVector velocity;
  PVector acceleration;
  PVector wind;
  // The Mover's maximum speed
  float mass;
  float topspeed;
  float ballonHeight, ballonWidth;
 
  // Wind Force variables - Perlin Noise
  float tx,ty;
  float x,y;
  
  
  Ballon() {
    // Start in the center
    position = new PVector(width/2,4*height/5);
    velocity = new PVector(0,0);
    acceleration = new PVector(0, -0.1);
    topspeed = 5;
    ballonHeight = 68;
    ballonWidth = 48;
    mass = 10;
  }

  void update() {
    x = map(noise(tx), 0, 1, -0.1, 0.1);
    wind = new PVector(x, -0.1);
    
    applyForce(wind);

    // Velocity changes according to acceleration
    velocity.add(acceleration);
    // Limit the velocity by topspeed
    velocity.limit(topspeed);
    // position changes by velocity
    position.add(velocity);
    
    tx += 0.01;
    ty += 0.01;
    acceleration.mult(0);

  }

  void display() {
    stroke(0);
    strokeWeight(2);
    fill(127,200);
    ellipse(position.x,position.y,ballonWidth,ballonHeight);
  }

  void checkCeiling(){
    if (position.y < 0 + ballonHeight/2) {
      velocity.y *= -1;
    }   
  }
  
   void applyForce(PVector force) {
    PVector f = PVector.div(force, mass);
    acceleration.add(f);
   }
   
   
}
