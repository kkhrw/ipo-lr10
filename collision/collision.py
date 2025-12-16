class RectCorrectError(Exception):
  pass
def isCorrectRect(coords):
  bottom_left, top_right = coords
  x1, y1 = bottom_left
  x2, y2 = top_right
  
  return x1 < x2 and y1 < y2



def isCollisionRect(rect1, rect2):
 
  if not isCorrectRect(rect1):
    raise RectCorrectError("1й прямоугольник некорректный")
  
  if not isCorrectRect(rect2):
    raise RectCorrectError("2й прямоугольник некорректный")
  
  x1, y1 = rect1[0]  
  x2, y2 = rect1[1] 
  
  x3, y3 = rect2[0]  
  x4, y4 = rect2[1]  
  
  return x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3
