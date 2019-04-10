// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

Mover[] movers = new Mover[20];
Mover mouseForce;

float g = 0.4;

void setup() {
  size(1280,720);
  for (int i = 0; i < movers.length; i++) {
    movers[i] = new Mover(random(0.1,2),random(width),random(height)); 
  }
}

void draw() {
  background(255);
  mouseForce = new Mover(50,mouseX,mouseY); 


  for (int i = 0; i < movers.length; i++) {
     PVector mF = mouseForce.attract(movers[i]);
     movers[i].applyForce(mF);


    for (int j = 0; j < movers.length; j++) {
      if (i != j) {
        PVector force = movers[j].repel(movers[i]);
        movers[i].applyForce(force);
      }
    }

    movers[i].update();
    movers[i].display();
  }

}
