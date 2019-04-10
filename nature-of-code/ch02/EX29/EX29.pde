// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

Mover[] movers = new Mover[1];

//Attractor a;

Attractor[] attractors = new Attractor[1];

void setup() {
  size(1280, 720);
  for (int i = 0; i < movers.length; i++) {
    movers[i] = new Mover(random(0.1, 2), random(width), random(height));
  }
  
  for (int i = 0; i < attractors.length; i++) {
    attractors[i] = new Attractor();
  }

}

void draw() {
  background(255,255,255);

  for (int i = 0; i < attractors.length; i++) {    
    attractors[i].display();
    attractors[i].drag();
    attractors[i].hover(mouseX, mouseY);
  }
  


  for (int i = 0; i < movers.length; i++) {
    for (int j = 0; j < attractors.length; j++) {
        PVector force = attractors[j].attract(movers[i]);
        println(force.mag());
        movers[i].applyForce(force);
    }
    
    movers[i].update();
    movers[i].display();
  }
}

void mousePressed() {  
  for (int i = 0; i < attractors.length; i++) {
    attractors[i].clicked(mouseX, mouseY);
  }
}

void mouseReleased() {
  for (int i = 0; i < attractors.length; i++) {
    attractors[i].stopDragging();
  }
}
