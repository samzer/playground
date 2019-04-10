class Mover {

  // The Mover tracks position, velocity, and acceleration
  PVector position;
  PVector velocity;
  PVector acceleration;
  float topspeed;
  float mass;


  Mover() {
    mass = 1;
  }

  void update() {
  }

  void display() {
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
