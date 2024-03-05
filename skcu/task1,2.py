import openpyxl
from openpyxl import Workbook
from datetime import datetime
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
  
wb = Workbook()
ws = wb.active
ws.title = "TDSheet"

ws.append(["Имя", "Текущая Дата", "Текущее время"])

names = ["Alinur","Yerbulan","Ayan","Dastan","Adilzhan","Alibek","Yernur","Alikhan","Daniyar","Yerasyl"]
current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")

for name in names:
    ws.append([name ,current_date,current_time])

random_number = random.randint(100, 999)
filename = f"names_{current_date}_{random_number}.xlsx"

filepath = f"C:\\Users\\awexe\\Documents\\skcu\\{filename}"

wb.save(filepath)


# Task 2: 
sender_email = "awexeoz7z@gmail.com" 
receiver_email = "alinurlpv@gmail.com" 
subject = "Excel File"
body = "Please find the Excel file attached."

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEBase("application", "octet-stream"))

with open(filepath, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")

msg.attach(part)

smtp_server = "smtp.gmail.com"  
smtp_port = 587 
smtp_username = "awexeoz7z@gmail.com" 
smtp_password = 'rjuo knag jgru sasi' 

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())