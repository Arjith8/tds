import streamlit as st

n1 = st.text_input('Input The 1st Number')
n2 = st.text_input('Input The 2nd Number')
n3 = st.text_input('Input The 3rd Number')

if n1 and n2 and n3:
    l = [n1, n2, n3]
    li =[int(i) for i in l]
    max = max(li)

    st.write('The Maximum Number is:', max)