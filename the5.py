import random
import streamlit as st

# 🟢 إصلاح 1: تهيئة القيم بشكل صحيح باستخدام علامة (=)
if 'button_text' not in st.session_state:
    st.session_state.button_text = "السؤال التالي"

if 'num' not in st.session_state:
    st.session_state.num = 0  # تم إضافة = 0

if 'sc' not in st.session_state:
    st.session_state.sc = 0  # تم إضافة = 0

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.sign = random.choice(['+', '-', '*', '/'])

num1 = st.session_state.num1
num2 = st.session_state.num2
sign = st.session_state.sign

# حساب النتيجة وحفظها في الـ session_state مباشرة لضمان استقرارها
if sign == '+':
    st.session_state.sc = num1 + num2
elif sign == '-':
    st.session_state.sc = num1 - num2
elif sign == '*':
    st.session_state.sc = num1 * num2
elif sign == '/':
    # استخدام القسمة الصحيحة // لتجنب الكسور الفاصلة إذا كنت تفضل ذلك
    st.session_state.sc = num1 // num2 

st.title("أهلاً بك في لعبتي 🎮")
st.write(f"ما هي نتيجة: {num1} {sign} {num2} ؟")

number = st.number_input("أدخل النتيجة", value=0, step=1)

if st.button("تأكيد التخمين", key="submit_btn"):
    st.session_state.count += 1
    if number == st.session_state.sc:
        st.success("إجابتك صحيحة! أحسنت 🌟")
        st.session_state.num += 1
    else:
        st.error(f"إجابتك خاطئة! الإجابة الصحيحة كانت: {st.session_state.sc} ❌")
        st.session_state.num = 0
    st.rerun()

# 🟢 إصلاح 2: إضافة key فريد للزر لمنع تداخل الأسماء
if st.button("السؤال التالي", key="next_q_btn_1"):
    del st.session_state.num1
    del st.session_state.num2
    del st.session_state.sign
    st.rerun()

if st.session_state.num == 10:
    st.success("لقد اجتزت هذا الليفل! 🎉")
    # 🟢 إصلاح 3: إضافة key فريد هنا أيضاً لأن الاسم قد يتشابه
    if st.button(st.session_state.button_text, key="next_level_btn"):
        if st.session_state.button_text == "السؤال التالي":
            st.session_state.button_text = "11"
            st.rerun()

st.write(f"Your points are {st.session_state.num} from {st.session_state.count} Questions")
