import turtle as trtl

# Making the rectangle base of the vending machine and coloring it

bigrect = trtl.Turtle()

bigrect.penup() # Cursor goes to the specific spot I want it to go
bigrect.fillcolor("gold")
bigrect.goto(-150,210)
bigrect.pendown()

bigrect.pensize(4) # Changed the color and size of tge outlines
bigrect.pencolor("saddlebrown")

bigrect.begin_fill()
bigrect.forward(290) # Makes the yellow rectangle
bigrect.circle(-10,90)
bigrect.forward(370)
bigrect.circle(-10,90) # This makes the round corners
bigrect.forward(290)
bigrect.circle(-10,90)
bigrect.forward(370)
bigrect.circle(-10,90)
bigrect.end_fill()

bigrect.hideturtle()

#Making the smaller rectangle inside the rectangle
lilrect = trtl.Turtle()

lilrect.penup() 
lilrect.fillcolor("palevioletred")
lilrect.goto(-145,185)
lilrect.pendown()

lilrect.pensize(4)
lilrect.pencolor("saddlebrown")

lilrect.left(270) # Had to make the cursor go down since it was up

lilrect.begin_fill()
lilrect.forward(270) # Makes the pinkish rectangle
lilrect.circle(10,90)
lilrect.forward(170)
lilrect.circle(10,90)
lilrect.forward(270)
lilrect.circle(10,90)
lilrect.forward(170)
lilrect.circle(10,90)
lilrect.end_fill()

lilrect.hideturtle()

# Making the 2 legs of the machine

legs = trtl.Turtle()

legs.penup()
legs.fillcolor("palevioletred")
legs.goto(-145,-190)
legs.pendown()

legs.pensize(4)
legs.pencolor("saddlebrown")

legs.right(90)

legs.begin_fill()
legs.forward(10) 
legs.circle(10,90)
legs.forward(40)
legs.circle(10,90)
legs.forward(10)
legs.circle(10,90)
legs.forward(40)
legs.circle(10,90)
legs.end_fill()

legs.hideturtle()

legs2 = trtl.Turtle() # Here is the second leg code is. 

legs2.penup()
legs2.fillcolor("palevioletred")
legs2.goto(135,-190)
legs2.pendown()

legs2.pensize(4)
legs2.pencolor("saddlebrown")

legs2.right(90)

legs2.begin_fill()
legs2.forward(10) 
legs2.circle(-10,90)
legs2.forward(40)
legs2.circle(-10,90)
legs2.forward(10)
legs2.circle(-10,90)
legs2.forward(40)
legs2.circle(-10,90)
legs2.end_fill()

legs2.hideturtle()

# Making the long rectangle under the the lilrect

longrect = trtl.Turtle()

longrect.penup()
longrect.fillcolor("palevioletred")
longrect.goto(-132,-110)
longrect.pendown()

longrect.pensize(4)
longrect.pencolor("saddlebrown")

longrect.begin_fill()
longrect.forward(170) 
longrect.circle(-10,90)
longrect.forward(15)
longrect.circle(-10,90)
longrect.forward(170)
longrect.circle(-10,90)
longrect.forward(15)
longrect.circle(-10,90)
longrect.end_fill()

longrect.hideturtle()

# Makes the square next to the long rectangle

square = trtl.Turtle()

square.penup()
square.fillcolor("palevioletred")
square.goto(90,-105)
square.pendown()

square.pensize(4)
square.pencolor("saddlebrown")

square.begin_fill()
count = 0
while (count < 4):
  square.forward(22)
  square.circle(-10,90)
  count = count + 1 
square.end_fill()

square.hideturtle()

# Makes the rectangle on the right side above the square

rectangle = trtl.Turtle()

rectangle.penup()
rectangle.fillcolor("palevioletred")
rectangle.goto(60,-50)
rectangle.pendown()

rectangle.pensize(4)
rectangle.pencolor("saddlebrown")

rectangle.right(90)

rectangle.begin_fill()
rectangle.forward(15) 
rectangle.circle(10,90)
rectangle.forward(55)
rectangle.circle(10,90)
rectangle.forward(15)
rectangle.circle(10,90)
rectangle.forward(55)
rectangle.circle(10,90)
rectangle.end_fill()

rectangle.hideturtle()

# Makes the blue circle inside the rectangle

bluecircle = trtl.Turtle()

bluecircle.penup()
bluecircle.fillcolor("light blue")
bluecircle.goto(98,-67)
bluecircle.pendown()

bluecircle.pensize(4)
bluecircle.pencolor("saddlebrown")

bluecircle.begin_fill()
bluecircle.circle(10)
bluecircle.end_fill()

bluecircle.hideturtle()

# It's the white rectangle with a line in the middle

whiterect = trtl.Turtle()

whiterect.penup()
whiterect.fillcolor("white")
whiterect.goto(65,10)
whiterect.pendown()

whiterect.pensize(4)
whiterect.pencolor("saddlebrown")

whiterect.begin_fill()
whiterect.forward(65) 
whiterect.circle(-10,90)
whiterect.forward(5)
whiterect.circle(-10,90)
whiterect.forward(65)
whiterect.circle(-10,90)
whiterect.forward(5)
whiterect.circle(-10,90)
whiterect.end_fill()

whiterect.hideturtle()

line = trtl.Turtle() # It makes the line in the center of the rectangle

line.penup()
line.fillcolor("white")
line.goto(69,-2)
line.pendown()

line.pensize(7)
line.pencolor("saddlebrown")

line.begin_fill()
line.forward(60) 
line.end_fill()

line.hideturtle()

# Makes the green triangle

triangle = trtl.Turtle() 

triangle.penup()
triangle.fillcolor("yellowgreen")
triangle.goto(73,40)
triangle.pendown()

triangle.pensize(4)
triangle.pencolor("saddlebrown")

triangle.begin_fill()
triangle.forward(50)
triangle.right(140)
triangle.forward(30)
triangle.right(72)
triangle.forward(35)
triangle.end_fill()

triangle.hideturtle()

# Makes the 3x3 circles

whitecircle = trtl.Turtle() 

whitecircle_list = []   # circle row 1
whitecircle_colors = ["white", "white", "white"]

whitecircleYloc = 100
for c in whitecircle_colors:
  whitecircle = trtl.Turtle()
  whitecircle_list.append(whitecircle)
  
  whitecircle.penup()
  whitecircle.fillcolor(c)
  whitecircle.goto(75,whitecircleYloc)
  whitecircle.pendown()

  whitecircle.pensize(4)
  whitecircle.pencolor("saddlebrown")

  whitecircle.begin_fill()
  whitecircle.circle(7)
  whitecircle.end_fill()
  
  whitecircle.hideturtle()
  whitecircleYloc -= 22

whitecircle_list = []   # circle row 2
whitecircle_colors = ["white", "white", "white"]

whitecircleYloc = 100
for c in whitecircle_colors:
  whitecircle = trtl.Turtle()
  whitecircle_list.append(whitecircle)
  
  whitecircle.penup()
  whitecircle.fillcolor(c)
  whitecircle.goto(100,whitecircleYloc)
  whitecircle.pendown()

  whitecircle.pensize(4)
  whitecircle.pencolor("saddlebrown")

  whitecircle.begin_fill()
  whitecircle.circle(7)
  whitecircle.end_fill()
  
  whitecircle.hideturtle()
  whitecircleYloc -= 22
  
whitecircle_list = []   # circle row 3
whitecircle_colors = ["white", "white", "white"]

whitecircleYloc = 100
for c in whitecircle_colors:
  whitecircle = trtl.Turtle()
  whitecircle_list.append(whitecircle)
  
  whitecircle.penup()
  whitecircle.fillcolor(c)
  whitecircle.goto(125,whitecircleYloc)
  whitecircle.pendown()

  whitecircle.pensize(4)
  whitecircle.pencolor("saddlebrown")

  whitecircle.begin_fill()
  whitecircle.circle(7)
  whitecircle.end_fill()
  
  whitecircle.hideturtle()
  whitecircleYloc -= 22



# Blue rectangle above the circles

bluerect = trtl.Turtle() 

bluerect.penup()
bluerect.fillcolor("light blue")
bluerect.goto(67,170)
bluerect.pendown()

bluerect.pensize(4)
bluerect.pencolor("saddlebrown")

bluerect.begin_fill()
bluerect.forward(60) 
bluerect.circle(-10,90)
bluerect.forward(20)
bluerect.circle(-10,90)
bluerect.forward(60)
bluerect.circle(-10,90)
bluerect.forward(20)
bluerect.circle(-10,90)
bluerect.end_fill()

bluerect.hideturtle()

# Makes the first row in the vending machine (chips)

chips = trtl.Turtle() 

chips_list = []   # create empty list
chips_colors = ["pink", "white", "lightblue"]

chipsXloc = -117
for c in chips_colors:
  chips_list.append(chips)
  
  chips.penup()
  chips.fillcolor(c)
  chips.goto(chipsXloc,178)
  chips.pendown()

  chips.pensize(4)
  chips.pencolor("saddlebrown")

  chips.begin_fill()
  chips.forward(15) 
  chips.circle(-10,90)
  chips.forward(25)
  chips.circle(-10,90)
  chips.forward(15)
  chips.circle(-10,90)
  chips.forward(25)
  chips.circle(-10,90)
  chips.end_fill()
  chips.hideturtle()

  chipsXloc += 60

# Making the stripes for the chips

stripes = trtl.Turtle()

stripes_list = []   
stripes_colors = ["white", "yellow", "white"]

stripesXloc = -120
for c in stripes_colors:
  stripes = trtl.Turtle()
  stripes_list.append(stripes)
  
  stripes.penup()
  stripes.goto(stripesXloc,141)
  stripes.pendown()

  stripes.left(35)

  stripes.pencolor(c)
  stripes.pensize(11)

  stripes.forward(26)

  stripes.hideturtle()

  stripesXloc += 60



stripes_list = []   #This is for the brown outline on the stripes
stripes_colors = ["saddlebrown", "saddlebrown", "saddlebrown"]

stripesXloc = -116
for c in stripes_colors:
  stripes = trtl.Turtle()
  stripes_list.append(stripes)
  stripes.penup()
  stripes.goto(stripesXloc,135)
  stripes.pendown()
  stripes.left(35)

  stripes.pensize(4)
  stripes.pencolor(c)
  stripes.forward(29)

  stripes.hideturtle()

  stripesXloc += 60




stripes_list = []  #This is for the brown outline on the stripes pt2
stripes_colors = ["saddlebrown", "saddlebrown", "saddlebrown"]

stripesXloc = -127
for c in stripes_colors:
  stripes = trtl.Turtle()
  stripes_list.append(stripes)
  
  stripes.penup()
  stripes.goto(stripesXloc,142)
  stripes.pendown()

  stripes.left(35)

  stripes.pensize(4)
  stripes.pencolor(c)
  stripes.forward(38)
  
  stripes.hideturtle()

  stripesXloc += 60

# This is the line under the chips

chipsline = trtl.Turtle()

chipsline.penup()
chipsline.goto(-130,128)
chipsline.pendown()

chipsline.pensize(5)
chipsline.pencolor("saddlebrown")

chipsline.forward(160)
chipsline.hideturtle()

# Makes the second row in the vending machine(candy)

candybar = trtl.Turtle() 

candybar_list = []  
candybar_colors = ["yellow", "orange", "lightgreen"]

candybarXloc = -110
for c in candybar_colors:
  candybar = trtl.Turtle()
  candybar_list.append(candybar)
  
  candybar.penup()
  candybar.fillcolor(c)
  candybar.goto(candybarXloc,106)
  candybar.pendown()

  candybar.pensize(4)
  candybar.pencolor("saddlebrown")

  candybar.begin_fill()
  candybar.right(120)
  candybar.forward(40)
  candybar.left(90) 
  candybar.forward(20)
  candybar.left(90) 
  candybar.forward(40)
  candybar.left(90)
  candybar.forward(20)
  candybar.end_fill()

  candybar.hideturtle()

  candybarXloc += 60

#Making the two wrappers on candy (top&bottom)

wrappers = trtl.Turtle() 

wrappers_list = []  #top wrapper
wrappers_colors = ["yellow", "orange", "lightgreen"]

wrappersXloc = -110
for c in wrappers_colors:
  wrappers = trtl.Turtle()
  wrappers_list.append(wrappers)
  
  wrappers.penup()
  wrappers.fillcolor(c)
  wrappers.goto(wrappersXloc,106)
  wrappers.pendown()

  wrappers.pensize(4)
  wrappers.pencolor("saddlebrown")

  wrappers.begin_fill()
  wrappers.left(99)
  wrappers.forward(12)
  wrappers.right(125)
  wrappers.forward(34)
  wrappers.right(125)
  wrappers.forward(14)
  wrappers.right(60)
  wrappers.forward(20)
  wrappers.end_fill()

  wrappers.hideturtle()

  wrappersXloc += 60

#bottom wrappers

wrappers2 = trtl.Turtle() 

wrappers2_list = []  #top wrapper
wrappers2_colors = ["yellow", "orange", "lightgreen"]

wrappers2Xloc = -130
for c in wrappers2_colors:
  wrappers2 = trtl.Turtle()
  wrappers2_list.append(wrappers2)
  
  wrappers2.penup()
  wrappers2.fillcolor(c)
  wrappers2.goto(wrappers2Xloc,71)
  wrappers2.pendown()

  wrappers2.pensize(4)
  wrappers2.pencolor("saddlebrown")

  wrappers2.begin_fill()
  wrappers2.right(150)

  wrappers2.forward(16)
  wrappers2.left(130)
  wrappers2.forward(34)

  wrappers2.left(124)
  wrappers2.forward(12)
  wrappers2.left(62)
  wrappers2.forward(18)
  wrappers2.end_fill() 

  wrappers2.hideturtle()

  wrappers2Xloc += 60

#Making the second line under the candybar

candyline = trtl.Turtle() 

candyline.penup()
candyline.goto(-130,48)
candyline.pendown()

candyline.pensize(5)
candyline.pencolor("saddlebrown")

candyline.forward(160)
candyline.hideturtle()

# Makine the 3rd row (cookies)

cookies = trtl.Turtle() 
 
cookies_list = []   # create empty list
cookies_colors = ["plum", "light blue", "pink"]

cookiesXloc = -117
for c in cookies_colors:
  cookies = trtl.Turtle()
  cookies_list.append(cookies)
  
  cookies.penup()
  cookies.fillcolor(c)
  cookies.goto(cookiesXloc,30)
  cookies.pendown()

  cookies.pensize(4)
  cookies.pencolor("saddlebrown")

  cookies.begin_fill()
  cookies.forward(15) 
  cookies.circle(-10,90)
  cookies.forward(25)
  cookies.circle(-10,90)
  cookies.forward(15)
  cookies.circle(-10,90)
  cookies.forward(25)
  cookies.circle(-10,90)
  cookies.end_fill()
  cookies.hideturtle()

  cookiesXloc += 60

# Making the top and bottom of the cookies

cookietb = trtl.Turtle() 

cookietb_list = []   # Top
cookietb_colors = ["gold", "gold", "gold"]

cookietbXloc = -127
for c in cookietb_colors:
  cookietb = trtl.Turtle()
  cookietb_list.append(cookietb)
  
  cookietb.penup()
  cookietb.fillcolor(c)
  cookietb.goto(cookietbXloc,30)
  cookietb.pendown()

  cookietb.pensize(4)
  cookietb.pencolor("saddlebrown")

  cookietb.left(90)

  cookietb.begin_fill()
  cookietb.forward(1) 
  cookietb.circle(-3,90)
  cookietb.forward(30)
  cookietb.circle(-3,90)
  cookietb.forward(1)
  cookietb.circle(-3,90)
  cookietb.forward(30)
  cookietb.circle(-3,90)
  cookietb.end_fill()
  cookietb.hideturtle()

  cookietbXloc += 60


cookietb_list = []   #bottom
cookietb_colors = ["gold", "gold", "gold"]

cookietbXloc = -127
for c in cookietb_colors:
  cookietb = trtl.Turtle()
  cookietb_list.append(cookietb)
  
  cookietb.penup()
  cookietb.fillcolor(c)
  cookietb.goto(cookietbXloc,-18)
  cookietb.pendown()

  cookietb.pensize(4)
  cookietb.pencolor("saddlebrown")

  cookietb.begin_fill()
  cookietb.right(90)
  cookietb.forward(1) 
  cookietb.circle(3,90)
  cookietb.forward(30)
  cookietb.circle(3,90)
  cookietb.forward(1)
  cookietb.circle(3,90)
  cookietb.forward(30)
  cookietb.circle(3,90)
  cookietb.end_fill()

  cookietb.hideturtle()

  cookietbXloc += 60

# Making the circle in the middle of the cookies

cookiecircle = trtl.Turtle() 

cookiecircle_list = []   #bottom
cookiecircle_colors = ["gold", "gold", "gold"]

cookiecircleXloc = -110
for c in cookiecircle_colors:
  cookiecircle = trtl.Turtle()
  cookiecircle_list.append(cookiecircle)
  
  cookiecircle.penup()
  cookiecircle.fillcolor(c)
  cookiecircle.goto(cookiecircleXloc,-2)
  cookiecircle.pendown()

  cookiecircle.pensize(4)
  cookiecircle.pencolor("saddlebrown")

  cookiecircle.begin_fill()
  cookiecircle.circle(7)
  cookiecircle.end_fill()

  cookiecircle.hideturtle()

  cookiecircleXloc += 60

# Makes the line under the cookies

cookieline = trtl.Turtle() 

cookieline.penup()
cookieline.goto(-130,-23)
cookieline.pendown()

cookieline.pensize(5)
cookieline.pencolor("saddlebrown")

cookieline.forward(160)
cookieline.hideturtle()

# Makes the 4th row (soda)

soda = trtl.Turtle() 

soda_list = []   # create empty list
soda_colors = ["white", "white", "white"]

sodaXloc = -117
for c in soda_colors:
  soda = trtl.Turtle()
  soda_list.append(soda)
  
  soda.penup()
  soda.fillcolor(c)
  soda.goto(sodaXloc,-42)
  soda.pendown()

  soda.pensize(4)
  soda.pencolor("saddlebrown")

  soda.begin_fill()
  soda.forward(10) 
  soda.circle(-10,90)
  soda.forward(20)
  soda.circle(-10,90)
  soda.forward(10)
  soda.circle(-10,90)
  soda.forward(20)
  soda.circle(-10,90)
  soda.end_fill()
  soda.hideturtle()

  sodaXloc += 60

#Making the top part of the soda
sodatop = trtl.Turtle() 

sodatop_list = []   # Top
sodatop_colors = ["pink", "yellowgreen", "light blue"]

sodatopXloc = -128
for c in sodatop_colors:
  sodatop = trtl.Turtle()
  sodatop_list.append(sodatop)
  
  sodatop.penup()
  sodatop.fillcolor(c)
  sodatop.goto(sodatopXloc,-44)
  sodatop.pendown()

  sodatop.pensize(4)
  sodatop.pencolor("saddlebrown")

  sodatop.left(90)

  sodatop.begin_fill()
  sodatop.forward(3) 
  sodatop.circle(-4,90)
  sodatop.forward(25)
  sodatop.circle(-4,90)
  sodatop.forward(2)
  sodatop.circle(-4,90)
  sodatop.forward(25)
  sodatop.circle(-4,90)
  sodatop.end_fill()
  sodatop.hideturtle()

  sodatopXloc += 60

#Making the 4th line (soda)
sodaline = trtl.Turtle() 

sodaline.penup()
sodaline.goto(-130,-84)
sodaline.pendown()

sodaline.pensize(5)
sodaline.pencolor("saddlebrown")

sodaline.forward(160)
sodaline.hideturtle()

# Asking what you want from the vendng machine
name = input("Hello! Would you like to get something from the vending machine? Y/N")
if name =="N":
  if name=="Y":
    print("Ok, bye!!")
else:
  print("What would you like from the vending machine? (chips,candybar,cookies, & soda)")

wn = trtl.Screen()
wn.mainloop()
