import streamlit as st


def app():
    st.title('Home')
    with st.container():
        st.title('Customer churn finder for telco company!')
        st.subheader('By Anirudh :wave:') 
    
    with st.container():
        st.title('What is customer churn :information_source:')
        st.write('When a customer stops doing business with the company the customer is churned.The buisness are keen in keeping the existing customer because it is far less resource consuming than aquiring a new customer. Existing customers will often have a higher volume of service consumption and can generate additional customer referrals. Customer churn can be resovled by giving a good product and services.Preventing customer churn is critically important in telecommunication sector in retail as barriers to entry switching services and provider are so low. Acquire different datasets from kaggle, IBM sample datasets, Google dataset sample etc.. ')
        

