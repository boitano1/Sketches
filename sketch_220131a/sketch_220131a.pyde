speed = 1000
x_dim = 1000
y_dim = 1000

diameter = 20

def setup():
  size(x_dim, y_dim)
  colorMode(RGB, x_dim)
  background(0)

def draw():
  r = pmouseX
  g = pmouseY
  b = 300

  fill(r, g, b)
  noStroke()
  ellipse(random(-speed, speed), random(-speed, speed), diameter, diameter)
  
  return r, g, b
