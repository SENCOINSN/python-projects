#! /usr/bin/python3

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.application import MIMEApplication 

import logging


subject="ENVOI CV"

send_email="seyeadam1@gmail.com"

smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_password="dbtkdtifdczkutvq"
path_file="cv_adama_seye.pdf"

enought = False

while  not enought :
    poste = input(" Quel est le poste à inclure ? ")
    recipient = input(" Quel est l'adresse destinataire ? ")
    if poste != "" and recipient != "":
        enought = True
        break
        
else:
    print("Tous les champs sont obligatoires")


print("Process envoi email !!! ")

body = "Bonjour, je vous envoies mon cv suite à votre annonce pour le poste "+poste+"\n .Pour plus d'information, vous pourrez me contacter sur le numéro mentionné sur le cv. Merci\n Cordialement"

message = MIMEMultipart()

message["From"] = send_email
message["To"] = recipient
message["Subject"] = subject

body_part = MIMEText(body, "plain") 

message.attach(body_part)

with open(path_file, "rb") as file:
    message.attach(MIMEApplication(file.read(), Name=path_file))

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(send_email, smtp_password)
    server.sendmail(send_email, recipient, message.as_string())  
    print("Email envoyé avec succés !!! ")
    