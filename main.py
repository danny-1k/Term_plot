import numpy as np
import matplotlib.pyplot as plt

class Termplot:
    def __init__(self,y,x=None,cols=50,rows=50,char='.'):
        self.x = x or list(range(len(y)))
        self.y = y
        self.cols = cols
        self.rows = rows
        self.char = char
        self.canvas = [[' ' for i in range(cols)] for i in range(rows)]

    def scale(self,nums,range_):
        return (range_-1)*(nums/max(nums))

    def draw(self):
        x = self.scale(np.array(self.x),self.cols)
        y = self.scale(np.array(self.y),self.rows)
        for i,j in zip(x,y):
            self.canvas[int(self.rows-j-1)][int(i)] = self.char
            
        print(f".{'~'*(self.cols)}.")
        for i in self.canvas:
            print(f"|{''.join(i)}|")
        print(f".{'~'*(self.cols)}.")