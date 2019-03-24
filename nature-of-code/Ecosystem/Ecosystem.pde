Rabbit[] rabbits = new Rabbit[20];
Snake[] snakes = new Snake[10];
Fly[] flies = new Fly[10];


void setup() {
 size(1280, 720);
 for (int i = 0; i < rabbits.length; i++) {
    rabbits[i] = new Rabbit();
  }

  for (int i = 0; i < snakes.length; i++) {
    snakes[i] = new Snake();
  }

  for (int i = 0; i < flies.length; i++) {
    flies[i] = new Fly();
  }
}

void draw() {
  background(255);
  for (int i = 0; i < rabbits.length; i++) {
    rabbits[i].draw();
  }

  for (int i = 0; i < snakes.length; i++) {
    snakes[i].draw();
  }

  for (int i = 0; i < flies.length; i++) {
    flies[i].draw();
  }
}
