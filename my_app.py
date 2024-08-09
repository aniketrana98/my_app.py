import streamlit as st

st.write("Hello World: Getting Bore, Hello Brother!!")
st.title("Display Title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader To write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text")
#To create hyperlink
st.markdown("[Streamlit](https://streamlit.io)")
st.markdown("[Streamlit CheatSheet](https://cheat-sheet.streamlit.app/)")
st.success("Success!")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error!")


from PIL import Image
img = Image.open("smj.jpg")
st.image(img, width=300, caption="Satyamev Jayate")

video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://youtu.be/UX3YrOB_gQA?si=aCewSgnsqrYut_T8")


audio_file = open("song.mp3","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("play")

st.header("Button Widgets")

if st.button("play1"):
   st.text("Hello World")

if st.button("play2"):
   st.text("Enjoy Music")
   st.video("https://youtu.be/oWYi39WRnNU?si=TkqGUEbayG3tkbT0")  

if st.checkbox("Checkbox"):
    st.text("checkbox selected")
#------#
radio_but = st.radio("your selection",["Male","Female"])
if radio_but == "Male":
    st.info("you are Male")
else:
    st.info("you are Female")

city = st.selectbox("your city",["Daman","Diu","Valsad"])
if city == "Daman":
    st.info("I love Daman")
elif city =="Diu":
    st.info("I love Diu")
else:
   st.info("I love Valsad")

occupation = st.multiselect("Your occupation",["Programmer","Data Scientist","ITConsultant","DBA"])


age = st.number_input("Input a number")


message =st.text_area("About NIELIT","WRITE SOMETHINGS----")
message =st.text_area("Address","WRITE SOMETHINGS----")

select_val = st.slider("select a value", 1, 10)
# satarting value = 10.0 ending value = 20.0 increment by =0.5
select_val1 = st.slider("select a value", 10.0, 20.0, 0.5)
if st.button("Balloons"):
    st.ballons()



#------Pandas DataFrame------#
import streamlit as st
import pandas as pd

auto_data=pd.read_csv("auto.csv")
st.dataframe(auto_data.head())

st.table(auto_data.head(10))

st.area_chart(auto_data[["mpg","cylinders"]])
st.area_chart(auto_data[["mpg","cylinders"]].head(20))

st.bar_chart(auto_data[["mpg","cylinders"]])
st.bar_chart(auto_data[["mpg","cylinders"]].head(20))

st.line_chart(auto_data[["mpg","cylinders"]])
st.line_chart(auto_data[["mpg","cylinders"]].head(20))

import datetime
import time

today = st.date_input("Today is",datetime.datetime.now())
hour = st.time_input("The time is",datetime.time(12,30))

st.code("import pandas as pd")
st.code("print(welcome to NITELIT Daman)")

import pandas as pd 
import numpy as np

st.title("Area")
df=pd.DataFrame(np.random.randn(40,4), columns=["C1","C2","C3","C4"])
st.bar_chart(df)

st.title("Line Chart")
df=pd.DataFrame(np.random.randn(40,4), columns=["C1","C2","C3","C4"])
st.line_chart(df)