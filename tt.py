import streamlit as st
import time
# import random
import matplotlib.pyplot as plt
import numpy as np

col1, col2, col3 = st.columns(3)

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'perple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['o', '^', 's', 'p'])

fig,ax = plt.subplots()

love = []
y = []
for i in range(-20, 21, 3):
    love.append(i)
    y.append(-2*i*i+ 3*i + 5)

# plt.plot(x, y, 'r:h')
plt.plot(love, y, color = c1, linestyle = s1, marker = m1)

st.pyplot(fig)


# x = []
# y = []
# ysin = []
# for i in range(-20, 21, 1):
#     x.append(i)
#     y.append(3*i*i - 5*i + 2)
#     ysin.append(1200*np.sin(i))

# plt.plot(x ,y, 'rs-', label = '2nd Equation')
# plt.plot(x, ysin, 'go--', label = 'sin Function')
# plt.legend()
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.xlim([-15,15])
# plt.ylim([-2000,2000])
# st.pyplot(fig)


# option = st.selectbox(
#      'How would you like to be contacted?',
#      ('2차 방정식', 'sin 함수', 'cos 함수'))
# st.write('You selected:', option)

# for i in x:
#     if '2차' in option:
#         y.append(a*i**2 + b*i + c)
#     if 'sin' in option:
#         y.append(np.sin(i))
#     if 'cos' in option:
#         y.append(np.cos(i))
# plt.plot(x,y)

# st.pyplot(fig)


# import streamlit as st

# agree = st.checkbox('I agree')

# if agree:
#     st.write('Great!')


# import streamlit as st

# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', option)


# st.title('tt')
# st.header('hh')


# import streamlit as st

# start_color, end_color = st.select_slider(
#     'Select a range of color wavelength',
#     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
#     value=('red', 'blue'))
# st.write('You selected wavelengths between', start_color, 'and', end_color)


# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "col1": np.random.randn(1000) / 50 + 37.76,
#     "col2": np.random.randn(1000) / 50 + -122.4,
#     "col3": np.random.randn(1000) * 100,
#     "col4": np.random.rand(1000, 4).tolist(),
# })

# st.map(df,
#     latitude='col1',
#     longitude='col2',
#     size='col3',
#     color='col4')


# import streamlit as st

# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")


# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

# st.dataframe(df.style.highlight_max(axis=0))


# st.write('# :green[**Hello**], *World!* :sunglasses:')
# st.write('## :blue[**Hello**], *World!* :sunglasses:')
# st.write('### :red[**Hello**], *World!* :sunglasses:')
# st.write('#### :orange[**Hello**], *World!* :sunglasses:')
# st.write('##### **Hello**, *World!* :sunglasses:')
# st.write('###### **Hello**, *World!* :sunglasses:')


import streamlit as st

# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)


import sys
sys.exit()

import streamlit as st
import time
# import random
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

x= []
for i in range(-3, 4):
    x.append(i/10.0)

col =st.columns(3)
with col[0]:
    a = st.number_input('Insert a', step = 10)
with col[1]:
    b = st.number_input('Insert b', step = 10)
with col[2]:
    c = st.number_input('Insert c', step = 10)
    
y = []
for i in x:
    y.append(a*i**2 + b*i + c)

plt.plot(x,y)

st.pyplot(fig)

# fig,ax = plt.subplots()
# numers = []
# for i in range(10):
#     numbers.append(random.randint(1,10))
# plt.plot(numbers)
# plt.ylabel('some random numbers')
# plt.xlabel('x-axis')
# st.pyplot(fig)

# s= [3, 7, 1, 9, -3, 3, 10]
# s
# a= np.sort(s)
# a1 = np.std(s)
# a

# a = sum(s)
# 'sum', a
# mx = max(s)
# 'max', mx
# mn = min(s)
# 'min', mn


# mx = -1e10
# mx
# for i in s:
#     if i > mx:
#         mx = i
# mx


# t = 0
# for i in s:
#     # t = t+ i
#     t +=i
# t

# s1 = 1
# s2 = 2
# s3 = 3
# s4 = 4
# s5 = 5
# s1, s2, s3, s4, s5

# s = ['a', 'b', 'c', 'd', 'e']

# s.append('사과')
# s.remove('c')
# s
# i = s.index('d')
# i



# s[-1]

# if 'f' not in s:
#     '1'
# else:
#     '2'

# import turtle

# def tree(length):
#     if length > 5:
#         t.forward(length)
#         t.right(20)
#         tree(length-15)
#         t.left(40)
#         tree(length-15)
#         t.right(20)
#         t.backward(length)

# t = turtle.Turtle()
# t.left(90)

# t.color('green')
# t.speed(0)
# tree(90)

# import turtle

# t = turtle.Turtle()
# # t.speed(1)
# t.shape('turtle')
# t.color((r.random(), r.random(), r.random()))

# t.forward(100)

# turtle.done()


# import turtle
# import random
# t = turtle.Turtle()

# t.speed(0)
# t.pensize(5)
# t.goto(0,0)

# def shape(sh):
#     for j in range(sh):
#         t.forward(1+5*i)
#         t.left(360/sh)


# while True:
#      for i in range(30):
        # t.circle(1+5*i)
        # t.forward(1 +5*i)
        # t.left(90)
        # t.forward(1 +5*i)
        # t.left(90)
        # t.forward(1 +5*i)
        # t.left(90)
        # t.forward(1 +5*i)
        # t.left(90)
    #     if i < 10:
    #         shape(3)
    #     elif i < 20:
    #         shape(4)
    #     elif i < 30:
    #         # shape(5)
    #         t.circle(1+5*i)
    #     t.color((r.random(),r.random(),r.random()))
    #     t.goto(i*20,0)
    #  t.clear()

    #  turtle.done()


# import turtle

# screen = turtle.Screen()
# # im1 = 'r.gif'
# # im2 = 'turtle.gif'

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()

# screen.addshpae(im1)
# screen.addshpae(im2)
# # screen.addshpae()

# t1.shape(im1)
# t2.shape(im2)
# # t3.shape()

# t1.penup()
# t1.shapesize(3)
# t1.pensize(5)
# t1.goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2.goto(-300,-100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2.goto(-300,-300)

# t1.pendown()
# t2.pendown()
# t3.pendown()
# t1.speed(1)
# t2.speed(1)
# t3.speed(1)


# for i in range(50):
#     d1 = r.randint(1,30)
#     t1.forward(d1)
#     d2 = r.randint(1,30)
#     t2.forward(d2)
#     d3 = r.randint(1,30)
#     t3.forward(d3)


#  for _ in range(6):
#      a1 = r.randint(1,45)
#      a2 = r.random()
#      a1,a2

# a = 0
# n = 10
# for i in range(n):
#     c = r.choice('abcdef')
#     if c == 'a':
#        a = a + 1 


# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)

# def rec(x, y, lx, ly):
#     turtle.bgcolor('yellow')
#     t.width(3)
#     t.color('blue')
#     t.fillcolor('green')
#     t.up()
#     t.goto(x,y)
#     t.down()
#     for i in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)

# rec(-200,0,100,50)
# rec(0,0,100,150)
# rec(200,0,100,100)

# turtle.done()

# def user_sum(n):
#     s = 0
#     for i in range(1,n+1):
#      s = s+i
#     s

# user_sum(100)
# user_sum(200)

# # 1.
# '나는 '+str(12)+'개의 사과를 먹었다.'

# # 2.
# 'apple'+'grape'
# print('apple'*3)

# # 3.
# age = 20
# if age < 20
#    print('aa')
# else:
#    print('bb')

# # 4.
# for num in range(1.101):
#    if num % 5 == 2:
#       print(num)


# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)

# # colors = ['red','purple','blue','yellow','orange','green']

# t.width(2)
# # turtle.bgcolor('black')

# length = 5
# for i in range(100):
#     t.forward(length)
#     # t.pencolor(colors[length%6])
#     t.right(45)
#     length += 1


# n = 40
# ang = 360/n
# for i in range(n):
#     t.forward(80) # 80 : 픽셀(원의 반지름)
#     t.left(ang) # 60 : 각도

# turtle.done()


# for i in range(1, 10):
#     if i%3 == 1:
#         i

# s = 70
# if s >= 90:
#     st.write('귀하의 점수는'+str(s)+'점으로 :blue[A등급]입니다')
# elif s >= 80:
#     '귀하의 점수는'+str(s)+'점으로 :green[B등급]입니다'
# elif s >= 70:
#     '귀하의 점수는'+str(s)+'점으로 :orange[C등급]입니다'
# elif s >= 60:
#     '귀하의 점수는'+str(s)+'점으로 :blue[D등급]입니다'
# else:
#     '귀하의 점수는'+str(s)+'점으로 :red[F등급]입니다'

# else: 
#     '# 귀하의 점수는'+str(s)+'점으로 :red[불합격]입니다'
#     '## 귀하의 점수는'+str(s)+'점으로 :red[불합격]입니다'
#     '### 귀하의 점수는'+str(s)+'점으로 :red[불합격]입니다'
#     '#### 귀하의 점수는'+str(s)+'점으로 :red[불합격]입니다'
#     '##### 귀하의 점수는'+str(s)+'점으로 :red[불합격]입니다'
#     '###### 귀하의 점수는'+str(s)+'점으로 :red[불합격]입니다'

# a = 1
# b = '1 '
# c = "1"

# b+c

# print('a=',a)
# 'a=',a
# b
# c

# a = 3

# a != 3

# x = 100

# x += 5
# x -= 10
# x 

# s = 0 # 초기값
# for i in range(1, 101, 2):
    # 's = ', s, 'i = ', i
    # s = s + i
    # s += i
    # 's + i = ', s
# s

# s = 1+2+3+4+5
# s

# '7과 4의 산술 연산'

# '덧셈', 7 + 4
# '뺄셈', 7 - 4
# '곱셈', 7 * 4
# '나눗셈', 7 / 4
# '몫', 7 // 4
# '나머지', 7 % 4
# '거듭제곱', 2 ** 4

# r = 20
# area = 3.14*r*r
# area

# x = 100
# x
# y = x+100
# y

# x = y+100
# x

# import turtle
# t = turtle.Turtle()
# t.shape('turtle')


# st.write('스트림릿......')
# st.image('im.jpg......')
# a = 3.141592*10*10.0
# b = (1/100)*1234
# print(a,b)
# a,b
# print('Hello')
# st.write('Hello')
# st.write('강아지'+'고양이')
# st.write('1'+'1')
# st.write(1+1)