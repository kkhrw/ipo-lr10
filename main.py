from collision import collision as c
  
# isCorrectRect
print(c.isCorrectRect([(-3.4, 1),(9.2, 10)])) # Вернет True
print(c.isCorrectRect([(-7, 9),(3, 6)])) # Вернет False

# isCollisionRect
print(c.isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))  # True
print(c.isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]))              # False

try:
    print(c.isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]))  # Ошибка
except c.RectCorrectError as e:
    print("Ошибка в isCollisionRect:", e)

# intersectionAreaRect
print(c.intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))
print(c.intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))

try:
    print(c.intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
except ValueError as e: 
    print("Ошибка в intersectionAreaRect:", e)

# intersectionAreaMultiRect с некорректным прямоугольником
incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]
]
try:
    c.intersectionAreaMultiRect(incorrect_rectangles)
except c.RectCorrectError as e:
    print("Ошибка в intersectionAreaMultiRect:", e)