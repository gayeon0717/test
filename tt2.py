import streamlit as st

x = []
for i in range(29,30,3):
    x.append(i)


import streamlit as st
import matplotlib.pyplot as plt

a = st.number_input('a의 값을 입력하시오', ['value=2.0', 'step=1.0'])
b = st.number_input('b의 값을 입력하시오', ['value=-1.0', 'step=1.0'])
c = st.number_input('c의 값을 입력하시오', ['value=15.0', 'step=1.0'])
d = st.number_input('d의 값을 입력하시오', ['value=2000.0', 'step=100.0'])

x = []
y = []
for i in range(-1.0,100,4):
    x.append(i)
    y.append(k)

plt.plot(x,y)


import matplotlib.pyplot as plt

xlist = []
for i in range(-100, 100):
    xlist.append(i/10.0)

a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

ylist = []
for i in zlist:
    ylist.append(a*i**2 + b*i + c)

plt.plot(xlist, ylist)
plt.show()


import matplotlib.pyplot as plt
import streamlit as st

fig,ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'purple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['o', '^', 's', 'p'])

love = []
y = []
for i in range(-20,21,3):
    love.append(i)
    y.append(-2*i*i + 3*i + 5)

plt.plot(love, y, color = c1, linestyle = s1, marker = m1)

st.pyplot(fig)