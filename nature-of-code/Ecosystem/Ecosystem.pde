Rabbit[] rabbits = new Rabbit[10];
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
  PVector force;
  
  for (int i = 0; i < rabbits.length; i++) {
    
    for(int j = 0; j < snakes.length; j++) {
        force = snakes[j].repel(rabbits[i]);
        rabbits[i].applyForce(force);
    }
    
    for(int j = 0; j < flies.length; j++) {
        force = flies[j].repel(rabbits[i]);
        rabbits[i].applyForce(force);
    }
    
    rabbits[i].draw();
  }

  for (int i = 0; i < snakes.length; i++) {
    for(int j = 0; j < rabbits.length; j++) {
        force = rabbits[j].attract(snakes[i]);
        snakes[i].applyForce(force);
    }
    
    snakes[i].draw();
  }

  for (int i = 0; i < flies.length; i++) {
    for(int j = 0; j < rabbits.length; j++) {
        force = rabbits[j].attract(flies[i]);
        flies[i].applyForce(force);
    }
    
    flies[i].draw();
  }
}
