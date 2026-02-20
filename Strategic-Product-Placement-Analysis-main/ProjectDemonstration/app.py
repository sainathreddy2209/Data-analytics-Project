from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# 🔑 CHANGE THESE VALUES
SENDER_EMAIL = "radhikagrandi31@gmail.com"
SENDER_PASSWORD = "ihuvnspsezljgfnf"  # Use Gmail App Password
RECEIVER_EMAIL = "grandisanthoshi31@gmail.com"  # Where you want to receive messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Email content
    subject = "New Contact Form Submission 🚀"
    body = f"""
    You received a new message from your website:

    Name: {name}
    Email: {email}
    Message: {message}
    """

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Gmail SMTP Server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
