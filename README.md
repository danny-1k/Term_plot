# Termplot
A simple script to draw line plots in the terminal

## Usage

```python
y = [2,4,6,3,4,5,6]
plot = Termplot(y,x=None,cols=15,rows=15,char='+')
plot.draw()
'''
Output
.~~~~~~~~~~~~~~~.
|    +         +|
|               |
|           +   |
|               |
|  +      +     |
|               |
|               |
|       +       |
|               |
|+              |
|               |
|               |
|               |
|               |
|               |
.~~~~~~~~~~~~~~~.
'''
```