import random
import streamlit as st
if 'ran' not in st.session_state:
  st.session_state.ran=20
if 'num' not in st.session_state:
  st.session_state.num=0
if 'sc' not in st.session_state:
  st.session_state.sc=0
if 'count' not in st.session_state:
  st.session_state.count=0
if 'num1' not in st.session_state:
 st.session_state.num1=random.randint(1,st.session_state.ran)
 st.session_state.num2=random.randint(1,st.session_state.ran)
 st.session_state.sign=random.choice(['+','-','*','/'])
num1=st.session_state.num1
num2=st.session_state.num2
sign=st.session_state.sign
if sign=='+':
 sc=num1+num2
if sign=='-':
 sc=num1-num2
if sign=='*':
 sc=num1*num2
if sign=='/':
 sc=num1/num2
st.title("أهلا بك في لعبتي ")
st.write(num1,sign,num2)
number=st.number_input("ادخل النتيجه ")
if st.button("تأكيد التخمين "):
  st.session_state.count += 1
  if number == sc:
    st.success("اجابتك صحيحه ! لقد احسنت")
    st.session_state.num += 1
  else:
    st.error(f"اجابتك خاطئة! الإجابة الصحيحة كانت : {sc}")
    st.session_state.num = 0
if st.button("السؤال التالي "):
    del st.session_state.num1
    del st.session_state.num2
    del st.session_state.sign
    st.rerun()
if st.session_state.num==1:
  st.success("لقد اجتزت هذا الليفل ")
  if st.button("الليفل التالي "):
     st.session_state.ran+=20
       del st.session_state.num1
        del st.session_state.num2
        del st.session_state.sign
st.write("your points are " ,st.session_state.num,"from",st.session_state.count,"Questions")
