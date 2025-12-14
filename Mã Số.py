from turtle import *
import time

# 定义绘图区域
setup(500, 700, startx=None, starty=None)
screensize(bg='wheat')
pencolor("#01863f")
pensize(12)
speed("fastest")

# 定义画笔起点
x = 0 
y = 260

# 定义圆圈尺寸颜色
length = 12

# 画第一层
# 拿起笔 
penup()
# 移动到坐标点(0, 200)
goto(x, y)
# 定义画笔角度
seth(-120) 
# 放下笔
pendown()
# 循环画12笔，每笔长度10像素，偏移5度
for i in range(12):
    # 向当前画笔方向移动10像素
    fd(10)
    # 顺时针移动5度
    right(2)

penup()
goto(x,y)
seth(-60)
pendown()
for i in range(12):
    fd(10)
    left(2)

# 画第一层折线
penup()
goto(x-79, y-94)
pendown()
for i in range(2):
  seth(-40)
  for i in range(5):
      fd(10)
  seth(40)    
  for i in range(5):
      fd(10)

# 画第二层
pencolor("#01863f")
penup()
goto(x-50, y-122)
seth(-120)
pendown()
for i in range(8):
    fd(10)
    right(3)

penup()
goto(x+50, y-122)
seth(-60)
pendown()
for i in range(8):
    fd(10)
    left(3)

# 画第二层折线
penup()
goto(x-106, y-185)
pendown()
for i in range(3):
  seth(-45)
  for i in range(5):
      fd(10)
  seth(45)    
  for i in range(5):
      fd(10)

# 画第三层
pencolor("#01863f")
penup()
goto(x-80, y-220)
seth(-120)
pendown()
for i in range(8):
    fd(10)
    right(3)

penup()
goto(x+80, y-220)
seth(-60)
pendown()
for i in range(8):
    fd(10)
    left(3)

# 画第三层折线
penup()
goto(x-135, y-283)
pendown()
for i in range(4):
  seth(-48)
  for i in range(5):
      fd(10)
  seth(48)    
  for i in range(5):
      fd(10)

# 画第四层
pencolor("#01863f")
penup()
goto(x-120, y-310)
seth(-120)
pendown()
for i in range(8):
    fd(10)
    right(3)

penup()
goto(x+120, y-310)
seth(-60)
pendown()
for i in range(8):
    fd(10)
    left(3)

# 画第四层折线
penup()
goto(x-170, y-373)
pendown()
for i in range(5):
  seth(-46)
  for i in range(5):
      fd(10)
  seth(46)    
  for i in range(5):
      fd(10)

# 画树干
penup()
fillcolor('#5f3c23')
pencolor("#5f3c23")
goto(-25, -135)
pendown()
begin_fill()
seth(-90)
fd(100)
seth(0)
fd(50)
seth(90)
fd(100)
end_fill()

pensize(6)
# 画第一层球球
hideturtle()
pencolor('red')
fillcolor('red')
penup()    
goto(x-72, y-103)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x-30, y-133)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x+43, y-132)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+88, y-100)  
pendown()  
begin_fill()
circle(length)
end_fill()

# 画第二层球球
penup()    
goto(x-100, y-196)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x-60, y-228)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x+10, y-232)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+82, y-225)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+117, y-196)  
pendown()  
begin_fill()
circle(length)
end_fill()

# 画第三层球球
penup()    
goto(x-130, y-295)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x-90, y-328)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x-25, y-330)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+43, y-330)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+109, y-328)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+147, y-295)  
pendown()  
begin_fill()
circle(length)
end_fill()

# 画第四层球球
penup()    
goto(x-160, y-384)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x-126, y-422)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup()    
goto(x-55, y-421)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+15, y-400)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+85, y-420)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+155, y-423)  
pendown()  
begin_fill()
circle(length)
end_fill()

penup() 
goto(x+190, y-388)  
pendown()  
begin_fill()
circle(length)
end_fill()

def koc(x, y, size):
  pensize(3)
  pencolor("orange")
  penup()
  goto(x, y)
  pendown()
  begin_fill()
  fillcolor('yellow')
  for i in range(5):
      left(72)
      fd(size)
      right(144)
      fd(size)
  end_fill()

# 星星
seth(0)
koc(-6, 280, 20)
koc(20, 180, 10)
koc(-70, -70, 8)
koc(-30, -20, 10)
seth(10)
koc(50, -30, 12)
seth(-10)
koc(20, 30, 11)
koc(-15, 210, 10)
seth(30)
koc(-70, 80, 9)
koc(90, -90, 9)
koc(-140, -110, 12)
koc(20, 100, 11)

penup()
seth(0)
goto(190, -320)
pendown()

pencolor("#01863f")
write("Merry Christmas", align="right", font=("Arial", 50, "bold"))
done()
