from rec import Rec2, Square, Circle

rec_1 = Rec2(3, 4)
rec_2 = Rec2(12, 5)

print(rec_1.get_area2())
print(rec_2.get_area2())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

circle_1 = Circle(8)
circle_2 = Circle(21)

print(circle_1.get_area_circle(),
      circle_2.get_area_circle())

figures = [rec_1, rec_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area2())