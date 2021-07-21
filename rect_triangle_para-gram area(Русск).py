import turtle,time
turtle.hideturtle()
t1=turtle.Turtle()
t1.hideturtle()
wn=turtle.Screen()
wn.setup(1300,1000)
turtle.bgcolor('light blue')
text=turtle.Turtle()
text.color('blue')
text.hideturtle()
text.up()
text.goto(-300,400)
TEXT_FONT=('Arial',25,'bold')
text.write('Площадь геометрических фигур', font=TEXT_FONT)
TEXT_FONT=('Arial',20,'bold')
text.goto(-300,350)
text.write('Площадь прямоугольника: выбери цифру 1 ', font=TEXT_FONT)
text.goto(-300,300)
text.write('Площадь треугольника: выбери цифру 2', font=TEXT_FONT)
text.goto(-300,250)
text.write('Площадь параллелограмма: выбери цифру 3', font=TEXT_FONT)
image1=('rectangle.gif')
image2=('triangle.gif')
image3=('para_gram.gif') #down load image parallelogram from internet to your computer (the same directory, where youe execute file)
image4=('background1.gif')
def img(image):
    wn.addshape(image)
    t1.shape(image)
t1.up()
t1.goto(-200,-100)
def triangle():
    global base
    global h
    global Area
    base=float(wn.textinput('Площадь треугольника','base(основание)='))
    h = float(wn.textinput('Площадь треугольника','h(высота)='))
    Area=base*h/2
    print(Area)
    turtle.clear()

def rectangle():
    global base
    global h
    global Area
    base = float(wn.textinput('Площадь прямоугольника','base(основание)='))
    h = float(wn.textinput('Площадь прямоугольника','h(высота)='))
    Area=base*h
    print(Area)
    turtle.clear()

def parall_m():
    global base
    global h
    global Area
    base = float(wn.textinput('Площадь параллелограмма','base(основание)='))
    h = float(wn.textinput('Площадь параллелограмма','h(высота)='))
    Area=base*h
    print(Area)
    turtle.clear()
    
def spec(X1,Y1, X2,Y2, Z,str_name):

    turtle.up()
    turtle.color('blue')
    turtle.goto(X1,Y1)
    turtle.down()
    turtle.write(str_name,font=('Times New Roman',20,'bold'))
    turtle.up()
    turtle.goto(X2,Y2)
    turtle.write(Z, font=('Times New Roman',20,'bold'))
   
answer=wn.textinput('Ищем площадь','вводим: 1 или 2 или 3')
if answer==str('1'):
    t1.clear()
    t1.showturtle()
    img(image1)
    rectangle()
if answer==str('2'):
    t1.clear()
    t1.showturtle()
    img(image2)
    triangle()
if answer==str('3'):
    t1.clear()
    t1.showturtle()
    img(image3)
    parall_m()

spec(250,0,420,0,base,'основание=')
spec(250,-30,420,-30,h,'высота=')
spec(250,-60,420,-60,Area,'Площадь=')

while True:
    answer=wn.textinput('Хочешь продолжить','введи да или нет')
    if answer=='да':
        img(image4)
        turtle.clear()
        t1.clear()
        answer=wn.textinput('Ищем площадь','вводим: 1 или 2 или 3')
        if answer=='1':
            img(image1)
            rectangle()
        if answer=='2':
            t1.clear()
            img(image2)
            triangle()
        if answer=='3':
            t1.clear()
            img(image3)
            parall_m()
        spec(250,0,420,0,base,'основание=')
        spec(250,-30,420,-30,h,'высота=')
        spec(250,-60,420,-60,Area,'Площадь=')
      
    if answer=='нет':
         turtle.clear()
         t1.hideturtle()
         print("Расчет Окончен")
         turtle.color('red')
         turtle.hideturtle()
         turtle.goto(-200,0)
         turtle.write('THE END', font=('Times New Roman',105,'bold'))
         time.sleep(5)      
         break