import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("product_prices.csv", index=False)
    print("📁 Saved to product_prices.csv")

def send_email(deals, budget):
    sender = "vishwavardhinidumpeti@gmail.com"
    receiver = "vishwavardhinidumpeti@gmail.com"
    password = "skxg bcnt comu gylw"

    msg = MIMEMultipart()
    msg['Subject'] = f"🛍️ Product Deals Under ₹{budget}"
    msg['From'] = sender
    msg['To'] = receiver

    html = "<h3>Deals within your budget:</h3><ul>"
    for item in deals:
        html += f"<li><b>{item['name']}</b> - ₹{item['price']} (<a href='{item['url']}'>View</a>)</li>"
    html += "</ul>"

    msg.attach(MIMEText(html, 'html'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, msg.as_string())
        print("📧 Email sent successfully!")
    except Exception as e:
        print(f"❌ Email failed: {e}")
