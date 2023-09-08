import turtle as t


def create_polygon(size, sides):

    angle = 360 / sides

    for action in range(sides):
        t.left(angle)
        t.forward(size)


# create_polygon(15, 50)


def create_circle(size):
    create_polygon(size, 50)


create_circle(10)


input("...")
