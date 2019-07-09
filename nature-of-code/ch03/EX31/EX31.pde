Mover mover;

void setup() {
  size(640, 360);
  mover = new Mover();
}

void draw() {
  background(255);
  //rotate(PI/30.0);
  mover.update();
  mover.display();
}
