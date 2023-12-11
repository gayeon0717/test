import matplotlib.pyplot as plt
import streamlit as st

fig,ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'purple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['o', '^', 's', 'p'])

love = []
y = []
for i in range(-20, 21, 3):
    love.append(i)
    y.append(-2*i*i+ 3*i + 5)

# plt.plot(x, y, 'r:h')
plt.plot(love, y, color = c1, linestyle = s1, marker = m1)

st.pyplot(fig)
