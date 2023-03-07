import streamlit as st
import smtplib
import yoga as y
import playVid as pv
from gtts import gTTS
from streamlit_option_menu import option_menu
# conn = sqlite3.connect('data.db')
# c=conn.cursor()
import requests

def mailer(email):
    r,c = pv.retData()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("20dce125@charusat.edu.in", "PRUTHA3011")
    server.sendmail("20dce125@charusat.edu.in",
                f"{email}",
                f"Congratulationss for the successfull set of exercise!,You have done BicepCurls with no of reps = {r} and calories burnt is {c}..Thanks")
    server.quit()

def main():

    # rad = option_menu(
    #     "Fitness Tracker",
    #     # menu_icon="dumbbell.png",
    #     options = ["Exercise","Yoga","Enter Your Email","Did You Know"],
    #     orientation="horizontal",
    # )
    rad = st.sidebar.radio(
        "Fitness Tracker",
        # menu_icon="dumbbell.png",
        options = ["Exercise","Yoga","Enter Your Email","Did You Know"],
        # orientation="horizontal",
    )
    #img = pv.BicepCurls_counter()
    if rad =="Exercise":
        # st.header("Bicep Curls")
        col1, col2 = st.columns(2)
        with col1:
            img = pv.BicepCurls_counter()
            # img = pv.SitUps_counter()
            # img = pv.PushUps_counter()
            st.image(img)
        with col2:
            # st.success("A dog")
            col2.image("Resources/1.jpg")
            st.image("Resources/1.jpg")

    if rad =="Yoga":
        pass
        # var1 = gTTS(text="वर्तमान में वक्रासन कर रहे हैं", lang='hi')
        # var1.save("wel1.mp3")
        # audio_file = open("wel1.mp3", "rb")
        # st.audio(audio_file.read())
        # st.header("Vakrasana")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Tree Pose")
            img2 = y.p2()
            st.image(img2)
        # with col2:
        # st.success("Tree Pose")
        # col2.image("Resources/treePose.jpg")
        # col1.image("Resources/treePose.jpg")


    if rad =="Enter Your Email":
        email=st.text_input ("Enter your Email")
        if st.button('Submit'):
            # create_usertable()
            # add_userdata(email)
            mailer(email)
            st.success("Report successfully submitted to your email")

    if rad =="Did You Know":
        url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

        querystring = {"query": "tomato"}

        headers = {
            "X-RapidAPI-Key": "325525d30amsh9dbc37e9c1aa6ddp1b44ecjsned5212010b20",
            "X-RapidAPI-Host": "calorieninjas.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        st.title("Did You Know!!")
        st.write(response.text)

if __name__ == '__main__':
    main()