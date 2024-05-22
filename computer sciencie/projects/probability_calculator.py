import copy
import random

class Hat:
    def __init__(self, *args, **kwargs):
        #unpack arguments
        self.contents=[]
        #adding elements to self.contents
        for key, value in kwargs.items():
            self.contents.extend([key]*value)

    def draw(self, n:int):
        self.drawn = []
        #if n (draw balls) is greater than self.contents length
        if n > len(self.contents):
            self.drawn = self.contents[:]
            self.contents = []
            return self.drawn
        
        for i in range(n):
            choice = random.choice(self.contents)
            self.drawn.append(self.contents.pop(self.contents.index(choice)))
            
        return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #Number of success    
    success_count = 0
    
    #Loop of number of experiments
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        
        #draw ball from hat (class that recicve number of balls and color with a method that draw n balls)
        draw = hat_copy.draw(num_balls_drawn)
        
        #counting the balls drawn
        draw_count = {ball: draw.count(ball) for ball in set(draw)}
        
        success = True
        for ball, count in expected_balls.items():
            if draw_count.get(ball, 0) <count:
                success = False
                break
        
        #comparing if expected balls is in draw
        if success:
            success_count += 1
    
    #calculating the probability 
    prob = success_count / num_experiments
    
    return prob
        


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat1.draw(2)
result = experiment(hat1,{"red":2, "green":1},5,1000)
print(result)

  