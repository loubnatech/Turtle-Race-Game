from turtle import Turtle, Screen
import random

# المتسابقون
fekrone_red = Turtle()
fekrone_red.color("red")
fekrone_blue = Turtle()
fekrone_blue.color("blue")
fekrone_yellow = Turtle()
fekrone_yellow.color("yellow")
fekrone_green = Turtle()
fekrone_green.color("green")

# خط النهاية
finish_line = Turtle()
finish_line.pensize(6)
finish_line.penup()
finish_line.hideturtle()
finish_line.goto(470, 350)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(700)

# إعداد نافذة السباق
window = Screen()
window.setup(1000, 700)
window.title("رهان سباق السلاحف")

# إعداد السلاحف: وضع الشكل ورفع القلم
fkarene = [fekrone_red, fekrone_blue, fekrone_yellow, fekrone_green]
for fekrone in fkarene:
    fekrone.shape("turtle")
    fekrone.penup()

# وضع السلاحف في أماكنها
fekrone_red.goto(-470, 150)
fekrone_blue.goto(-470, 50)
fekrone_yellow.goto(-470, -50)
fekrone_green.goto(-470, -150)

# ألوان السلاحف واختيارات المستخدم
fkarene_colors = ["red", "blue", "yellow", "green", "الأحمر", "الأزرق", "الأصفر", "الأخضر"]

# حفظ اختيار المستخدم
while True:
    user_choice = window.textinput("اختيار السلحفاة الفائزة", "من تتوقع سيفوز بالسباق (الأحمر - الأزرق - الأصفر - الأخضر)").lower()
    if user_choice in fkarene_colors:
        if user_choice == "red" or user_choice == "الأحمر":
            user_choice = fekrone_red
        elif user_choice == "blue" or user_choice == "الأزرق":
            user_choice = fekrone_blue
        elif user_choice == "yellow" or user_choice == "الأصفر":
            user_choice = fekrone_yellow
        elif user_choice == "green" or user_choice == "الأخضر":
            user_choice = fekrone_green
        break

# التحرك بمسافة عشوائية
distances = [1, 2, 4, 5, 7, 9, 10, 15]
def move(fekrone):
    fekrone.forward(random.choice(distances))

# تشغيل السباق طالما لا أحد وصل خط النهاية
while fekrone_red.xcor() <= 470 and fekrone_blue.xcor() <= 470 and fekrone_yellow.xcor() <= 470 and fekrone_green.xcor() <= 470:
    for fekrone in fkarene:
        move(fekrone)

# تحديد الفائز
winner = None
for fekrone in fkarene:
    if fekrone.xcor() > 470:
        winner = fekrone
        break

# هل فاز المستخدم بالرهان؟
if user_choice == winner:
    window.bgcolor("#86d008")
    finish_line.penup()
    finish_line.goto(0, 0)
    finish_line.pendown()
    finish_line.write("You Win!", font=("Comic Sans", 25, "bold"), align="center")
else:
    window.bgcolor("pink")
    finish_line.penup()
    finish_line.goto(0, 0)
    finish_line.pendown()
    finish_line.write("You Lose!", font=("Comic Sans", 25, "bold"), align="center")

window.exitonclick()