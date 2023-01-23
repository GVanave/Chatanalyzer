import pandas as pd
from collections import Counter




def preprocess_file(files):
  pattern_5 = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}'
  new_data=[]
  for i in files:
    if re.search(pattern_5,i)!=None:
      new_data.append(i)
  pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}'
  pattern_1='\spm\s-\s'
  pattern_2='\sam\s-\s'
  message=[]
  
  for i in new_data:
    review=re.split(pattern, i)
    
    for j in review:
      if j =="":
        review.remove(j)
    

    for k in review:
      second_review=re.split(pattern_1,k)
      for l in second_review:
        if l =="":
          second_review.remove(j)
      for m in second_review:
        third_review=re.split(pattern_2,m)
        for n in third_review:
          if n =="":
            third_review.remove(n)
        message.append(third_review)
    


  final_message=[]
  
  for o in message:
    
    for p in o:
      final_message.append(p)
 
  
  All_dates=[]
  for date in files:
    dates=re.findall(pattern,date)
    All_dates.append(dates)

  Dates=[]
  for lists in All_dates:
    if len(lists)!=0:
      Dates.append(lists)
  

  

  final_date_time=[]
  final_time=[]
  
  for i in Dates:
    for j in i:
      fourth_review=j.split(",")
      date_time=fourth_review[0] + fourth_review[1]
      
      final_date_time.append(date_time)
  

  
  create_frame=({"User_message":final_message,
              "Date":final_date_time})
  dataframe=pd.DataFrame(create_frame)
  df=dataframe.rename(columns={"User_message":"message","Date":"Dates"})
  User_Name=[]
  Messages=[]


  pattern_6="\d{9,14}:\s"
  for i in df["message"]:
    words=re.split('([\w\W]+?):\s',i)
    if len(words)>=2:
      User_Name.append(words[1])
      Messages.append(words[2])
    else:
      User_Name.append("Group Notification")
      Messages.append(words[0])
  df["User"]=User_Name
  df["Messages"]=Messages


  df.drop("message",axis=1,inplace=True)
  df["Only_date"]=pd.to_datetime(df["Dates"]).dt.date
  df["Year"]=pd.to_datetime(df["Dates"]).dt.year
  df["Month_no"]=pd.to_datetime(df["Dates"]).dt.month
  df["Month"]=pd.to_datetime(df["Dates"]).dt.month_name()
  df["Day"]=pd.to_datetime(df["Dates"]).dt.day
  df["Day_name"]=pd.to_datetime(df["Dates"]).dt.day_name()
  df["Hours"]=pd.to_datetime(df["Dates"]).dt.hour
  return df



