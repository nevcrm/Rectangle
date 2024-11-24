#// Name: Marcus Bracken
#// Course: CIS261 Object Oriented Computer Programming I
#// Lab: Rectangle


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width

    def print_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print('* ' * self.width)
            else:
                print('* ' + '  ' * (self.width - 2) + '*')


def main():
    print("Rectangle Calculator")

    while True:
        try:

            height = int(input("Height: "))
            width = int(input("Width: "))

            rectangle = Rectangle(height, width)

            print(f"Perimeter: {rectangle.calculate_perimeter()}")
            print(f"Area: {rectangle.calculate_area()}")

            rectangle.print_rectangle()

            continue_choice = input("Continue? (y/n): ").strip().lower()
            if continue_choice != 'y':
                break

        except ValueError:
            print("Please enter valid integers for height and width.")


if __name__ == "__main__":
    main()
