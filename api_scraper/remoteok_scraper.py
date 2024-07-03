import requests
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import pandas as pd

BASE_URL = "https://remoteok.com/api"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',
}

def get_job_postings():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json()

def output_to_xls(data):
    filtered_data = []
    for job in data:
        filtered_job = {
            "slug": job.get("slug"),
            "id": job.get("id"),
            "epoch": job.get("epoch"),
            "date": job.get("date"),
            "company": job.get("company"),
            "company_logo": job.get("company_logo"),
            "position": job.get("position"),
            "tags": ", ".join(job.get("tags", [])),  
            "description": job.get("description"),
            "location": job.get("location", ""),
            "salary_min": job.get("salary_min", ""),
            "salary_max": job.get("salary_max", ""),
            "apply_url": job.get("apply_url", ""),
            "url": job.get("url", "")
        }
        filtered_data.append(filtered_job)
    
    # Convertir la lista de diccionarios filtrados a un DataFrame de pandas
    df = pd.DataFrame(filtered_data)
    
    # Guardar el DataFrame a un archivo Excel
    df.to_excel('remote_jobs.xlsx', index=False)

def send_email(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To']= COMMASPACE.join(send_to)
    msg['Date']=formatdate(localtime=True)
    msg['Subject']=subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
             part = MIMEApplication(fil.read(), Name=basename(f))
        part['Content-Disposition']=f'attachment; filename"{basename(f)}"'
        msg.attach(part)
    
    smtp =smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(send_from, 'password') # put password here
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

if __name__=="__main__":
    json = get_job_postings()[1:]
    output_to_xls(json)
    send_email('your_email@gmail.com',['recipient1@gmail.com', 'recipient2@gmail.com'],'Jobs Posting', 
               'Please, find attached a list of jobs posting to this email', files=['remote_jobs.xlsx']) # put your email and recipient emails here