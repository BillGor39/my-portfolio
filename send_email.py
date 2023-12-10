import smtplib
import ssl

message = """\
Subject: hi
i love you
"""
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_email = "hua9939@gmail.com"
    password = "tquvmzqahojfiawc"

    receiver = "z1575261124@gmail.com"

    # receiver = "huahua9939@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, message)

if __name__ == "__main__":
    send_email(message)


