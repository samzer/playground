Ballon ballon;


void setup() {
 size(1280, 720);
 ballon = new Ballon();
}

void draw() {
  background(255);
  ballon.update();
  ballon.checkCeiling();
  ballon.display();
}
