class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
        return self.width
    
    def set_height(self, height):
        self.height = height
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.width > 50:
            return "Too big for picture."
        string = ''
        for c in range(self.height):
            for r in range(self.width):
               string += '*'
            string += '\n'
        return string
    
    def get_amount_inside(self, obj):
        times = self.get_area() / obj.get_area()
        return int(times)
    
    def __str__(self) -> str:
        string = f"{__class__.__name__}(width={self.width}, height={self.height})"
        return string

class Square(Rectangle):
    def __init__(self, side: int, width=0, height=0):
        super().__init__(width, height)
        self.side = side
        self.width = self.side
        self.height = self.side
    
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        return True
    
    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width
        return self.width
    
    def set_height(self, height):
        self.side = height
        self.width = height
        self.height = height
        return self.height
    
    def __str__(self) -> str:
        string = f"{__class__.__name__}(side={self.side})"
        return string
    

