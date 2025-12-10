def isCorrectRect(coords):
  bottom_left, top_right = coords
  x1, y1 = bottom_left
  x2, y2 = top_right
  
  return x1 < x2 and y1 < y2


print(isCorrectRect([(-3.4, 1), (9.2, 10)]))
print(isCorrectRect([(-7, 9), (3, 6)]))  

def isCollisionRect(rect1,rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")
    
    x1_min, y1_min = rect1[0]
    x1_max, y1_max = rect1[1]
    x2_min, y2_min = rect2[0]
    x2_max, y2_max = rect2[1]

    if x1_max <= x2_min or x2_max <= x1_min or y1_max <= y2_min or y2_max <= y1_min:
        return False
    else:
        return True
        isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]) # Вернет True

isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]) # Вернет False

#isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]) # Вызовет ошибку