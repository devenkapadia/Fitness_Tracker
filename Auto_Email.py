import smtplib
# import A_FitnessTrainerGUI as ft

def mailer(email):
    # e,r,c = ft.data()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("fitnesstracker48000@gmail.com", "BinaryBrains@2002")
    server.sendmail("20dce125@charusat.edu.in",
                f"{email}",
                f"Congratulationss for the successfull set of exercise!,You have done 12 with no of reps = 10 and calories burnt is 781...Thanks")
    server.quit()

if __name__ == '__main__':
    mailer("devenkapadia1@gmail.com")