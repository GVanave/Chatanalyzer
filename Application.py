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

        # word cloud
        st.title("Word Cloud")
        cloud_img=create_stats.WordCloud(user_selected,df)
        fig,ax=plt.subplot()
        ax.imshow(cloud_img)
        st.pyplot(fig)


        # most commond words in chat
        st.title("most common words")
        commond_words_dataframe=create_stats.individual_common_words(user_selected,df)
        fig,aix=plt.subplot()
        ax.barh(commond_words_dataframe[0],commond_words_dataframe[1])
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Busy Months and Busy Days
        col1,col2=st.columns(2)

        with col1:
            st.header("Busy Months Analysis")
            Month_dataframe=create_stats.busy_months(user_selected,df)
            # this month dataframe has infomration about 12 months and count of number of times chatted in months
            months=Month_dataframe[0]
            months_count=Month_dataframe[1]
            fig,ax=plt.subplot()
            ax.bar(months,months_count)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            st.header("Busy Day Analysis")
            day_dataframe=create_stats.busy_day(user_selected,df)
            day=day_dataframe[0]
            day_count=day_dataframe[1]
            fig,ax=plt.subplot()
            ax.bar(day,day_count)
            plt.xticks(rotation="verticle")
            st.pyplot(fig)
        

        st.title("Monthly Timeline")
        time = create_stats.monthtimeline(user_selected, df)
        fig, ax = plt.subplots()
        ax.plot(time['Time'], time['Messages'], color='green')
        plt.xticks(rotation='vertical')
        plt.tight_layout()
        st.pyplot(fig)

