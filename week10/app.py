import streamlit as st
import pandas as pd
import joblib
data =joblib.load("week10/final_model.pkl")
loaded_model = data["model"]
loaded_threshold = data["threshold"]
st.title("Bank Marketing Prediction")
col1,col2 = st.columns(2)
with col1:
 st.title("Bank Marketing Prediction")
 
 age = st.number_input("سن مشتری", min_value=18, max_value=100, value=30)
 balance = st.number_input("موجودی حساب مشتری", value=2000)
 day = st.number_input("روز اخرین تماس در ماه", min_value=1, max_value=31, value=15)
 previous = st.number_input("تعداد تماس های قبلی  ", min_value=0, value=0)
 campaign = st.number_input("تعداد تماس های انجام شده در این کمپین", min_value=1, value=1)
 pdays=st.number_input("تعداد روزهای گذشته از آخرین تماس", min_value=-1, value=-1)
 job = st.selectbox("شغل مشتری", ["admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown"])
 marital = st.selectbox("وضعیت تاهل مشتری", ["divorced", "married", "single"])
with col2:
 education = st.selectbox("تحصیلات مشتری", ["primary", "secondary", "tertiary", "unknown"])
 default = st.selectbox("آیا مشتری اعتبار پیش فرض دارد؟", ["no", "yes"])
 housing = st.selectbox("آیا مشتری وام مسکن دارد؟", ["no", "yes"])
 loan = st.selectbox("آیا مشتری وام شخصی دارد؟", ["no", "yes"])
 contact = st.selectbox("نوع تماس با مشتری", ["cellular", "telephone", "unknown"])
 month = st.selectbox("ماه تماس با مشتری", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
 poutcome = st.selectbox("نتیجه تماس قبلی با مشتری", ["failure", "success", "other", "unknown"])
customer = pd.DataFrame({
    "age": [age],
    "balance": [balance],
    "day": [day],
    "previous": [previous],
    "campaign": [campaign],
    "pdays": [pdays],
    "job": [job],
    "marital": [marital],
    "education": [education],
    "default": [default],
    "housing": [housing],
    "loan": [loan],
    "contact": [contact],
    "month": [month],
    "poutcome": [poutcome]
})
if st.button("پیش‌بینی"):
    yes_proba = loaded_model.predict_proba(customer)[:, 1]

    if yes_proba[0] >= loaded_threshold:
        st.success("مشتری احتمالاً به پیشنهاد بانک پاسخ مثبت می‌دهد.")
    else:
        st.warning("مشتری احتمالاً به پیشنهاد بانک پاسخ مثبت نمی‌دهد.")

    st.write(
        "احتمال پاسخ مثبت:",
        round(yes_proba[0] * 100, 2),
        "%"
    )
