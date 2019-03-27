// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

Mover[] movers = new Mover[5];
Pocket[] pockets = new Pocket[20];

void setup() {
  size(400, 800);
  //randomSeed(1);
  for (int i = 0; i < movers.length; i++) {
    movers[i] = new Mover(random(1, 4), random(width), 0);
  }
  
  for (int i = 0; i < pockets.length; i++) {
    pockets[i] = new Pocket(random(40,80), random(100,300),random(100,700));
  }
}

void draw() {
  background(255);
  
  // Display the moving balls
  for (int i = 0; i < movers.length; i++) {

    PVector wind = new PVector(0.01, 0);
    PVector gravity = new PVector(0, 0.1*movers[i].mass);

    float c = 0.05;
    PVector friction = movers[i].velocity.get();
    friction.mult(-1); 
    friction.normalize();
    friction.mult(c);

    movers[i].applyForce(friction);
    movers[i].applyForce(wind);
    movers[i].applyForce(gravity);

    // Check within a pocket    
    for (int j = 0; j < pockets.length; j++) {
      if(pockets[j].checkWithinBox(movers[i].position)){
        movers[i].applyForce(pockets[j].friction);
      }      
    }

    movers[i].update();
    movers[i].display();
    movers[i].checkEdges();
  }
  
  // Display the pockets
    for (int i = 0; i < pockets.length; i++) {
        pockets[i].display();
    }
}
