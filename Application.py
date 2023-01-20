import streamlit as st
import pandas as pd
import Data_preprocessing
import matplotlib.pyplot as plt
import create_stats
st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file=st.sidebar.file_uploader("choose a file")

if uploaded_file is not None:
    file_data=uploaded_file.getvalue()

    # decode the data
    data=file_data.decode("utf-8")

    df=Data_preprocessing.preprocess_file(data)

    st.dataframe(df)

    user_list=df["User"].unique().tolist()
    user_list.remove("Group Notification")
    user_list.sort()
    user_list.insert(0,"Overall")


    user_selected=st.sidebar.selectbox("Show Analysis of",user_list)
    st.title("Whatsapp Chat Analysis of " + user_selected)


    if st.sidebar.button("Show Analysis"):
        total_messages,links,no_ommitted_messages=create_stats.Message_info(user_selected,df)
    col1,col2,col3=st.columns(3)


    with col1:
        st.header("No of Messages")
        st.title(total_messages)

    with col2:
        st.header("No of Links")
        st.title(links)
    with col3:
        st.header("No of ommitted Messages")
        st.title(no_ommitted_messages)

    if user_selected=="Overall":
        st.title("Busy User List")
        count_busy_user,busy_df=create_stats.find_busy_user(df)
        fig,ax=plt.subplot()
        col1, col2=st.columns(2)

        with col1:
            ax.bar(count_busy_user.index,count_busy_user.values,color="blue")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            st.dataframe(busy_df)


st.title("ganesh vanave")




st.write("we ahve paln to go toghrther")
st.selectbox("please select the user ",options=("ganesh","mayur","sachin"))
st.title("ganesh vanave")
st.title("mayur vaanve")