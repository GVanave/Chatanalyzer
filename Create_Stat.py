from collections import Counter
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd


url_extract=URLExtract()

def individual_common_words(define_user,data_frame):
  if define_user!="Overall":
    df=data_frame[data_frame["User"]==define_user]

    temp_data=df[(df["User"]!="Group Notification") | (df["User"]=="<Media omitted>")]

    file=open("/content/stop_hinglish.txt","r")
    file_data=file.read()

    file_data=file_data.split("\n")
    words=[]
    for mess in df["Messages"]:
      word=mess.lower().split()
      for i in word:
        if i not in file_data:
          words.append(i)
    create_dict=dict(Counter(words).most_common(20))
    common_words=pd.DataFrame(create_dict.items())
    return common_words



def Message_info(define_user,df):
  if define_user!="Overall":
    df=df[df["User"]==define_user]
  # total number of messages
  total_messages=df.shape[0]


  # Total number of links in messages
  links=[]
  for message in df["Messages"]:
    links.extend(url_extract.find_urls(message))

  # Total mediaimmitted message
  media_datafranme=df[df["Messages"]=="<media omitted>"]
  no_ommitted_messages=media_datafranme.shape[0]


  return total_messages,len(links),no_ommitted_messages


def find_busy_user(df):
  df=df[df["User"]!="Group Notification"]
  # most busy users
  count_busy_user=df["User"].value_counts().head()

  # compare the busy user based on percentage
  new_data=(df["User"].value_counts()/df.shape[0])*100


  new_df=pd.DataFrame(new_data)

  return count_busy_user, new_df





def create_word_cloud(define_user,df):
  if define_user!="Overall":
    df=df[df["User"]==define_user]

  # create object for word cloud 

  wc=WordCloud(width=600, height=600,min_font_size=9,background_color="white")

  df_wc=wc.generate(df["Messages"].str.cat(sep=" "))


  return df_wc


def month_time_analysis(df):
  temp = df.groupby(['Year','Month_nu','Month']).count()["Messages"].reset_index()
  time_list=[]
  for i in range(temp.shape[0]):
    month_name=temp["Month_nu"][i]
    year_name=temp["Year"][i]
    name=f"{month_name}-{str(year_name)}" 
    time_list.append(name)
  temp["Time"]=pd.DataFrame(time_list)
  return temp


def busy_months(define_user,df):
  if define_user != "Overall":
    df=df[df["User"] == define_user]
    count_busy_months=df["Month"].value_counts()

  return count_busy_months


def busy_day(define_user,df):
  if define_user != "Overall":
    df=df[df["User"] == define_user]
    count_busy_day=df["Day_name"].value_counts()

  return count_busy_day