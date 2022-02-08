angle = 0.0
offset = 250
scalar = 2
speed = .5

x_dim = 500
y_dim = 500
x = x_dim/2
y = y_dim/2

def setup():
  size(x_dim, y_dim)
  fill(0)
  background(100)


def draw():
    
  r = 255
  g = 255
  b = 50
  noStroke()
  fill(r, g, b)
  x = offset + cos(angle) * scalar
  y = offset + sin(angle) * scalar
  ellipse(x, y, 6, 6)
  angle += speed
  scalar += speed
  
  return r, g, b
