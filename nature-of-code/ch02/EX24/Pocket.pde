class Pocket {
  float len;
  PVector position;
  PVector friction;

  Pocket(float l, float x , float y) {
    len = l;
    position = new PVector(x,y);
    friction = new PVector(0, random(-0.9, 0.9));

  }
  
  void display() {
    stroke(0);
    strokeWeight(2);
    fill(0,10);
    rect(position.x,position.y,len * 2,len);
  }
  
  boolean checkWithinBox(PVector p){
  
    if( p.x > position.x && p.x < position.x + 2*len){
      if( p.y > position.y && p.y < position.y + len){
        return true;
      }
    }
    
    return false;
  }
  
}
