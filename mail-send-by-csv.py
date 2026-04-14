import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Function to read data from the CSV file
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Function to send emails with attachments
def send_email(to_email, subject, body, attachment_path):
    from_email = 'mhasalkarsneha@gmail.com'  # Replace with your email
    password = 'qqhy ujhj xcmj jitc'     # Replace with your email password
    smtp_server = 'smtp.gmail.com'        # Replace with your SMTP server

    # Set up the MIME objects
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach body
    message.attach(MIMEText(body, 'plain'))

    # Attach resume
    with open(attachment_path, 'rb') as resume:
        resume_attachment = MIMEApplication(resume.read(), Name='resume.pdf')
        resume_attachment['Content-Disposition'] = f'attachment; filename=resume.pdf'
        message.attach(resume_attachment)

    # Connect to SMTP server and send the email
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())

# Main script
csv_file_path = 'HRmail.csv'  # Replace with your CSV file path
resume_path = 'mhasalkarsnehaResume.pdf'  # Replace with your resume file path

# Read data from the CSV file
contacts = read_csv(csv_file_path)

for contact in contacts:
    to_email = contact['Email']  # Assuming 'Email' is the column header in your CSV
    subject = 'Application for Entry-Level IT Position'
    body = """
   Dear Sir/Madam,

Greetings!

My name is Rahul Verma, and I am reaching out to explore any entry-level or graduate opportunities within your organization.

I have recently completed my Bachelor’s degree in Electronics and Telecommunication Engineering from XYZ Institute of Technology. Along with my academic studies, I have developed skills in Python, basic Machine Learning concepts, and web technologies through coursework and projects.

I am highly motivated to start my career in a challenging and growth-oriented environment where I can apply my knowledge, enhance my skills, and contribute effectively to the organization.

Please find my resume attached for your review. I would welcome the opportunity to discuss my profile in more detail. I am available at your convenience and can be contacted at [rahul.verma.demo@outlook.com](mailto:rahul.verma.demo@outlook.com) or 9876543210.

Thank you for your time and consideration.

Warm regards,
Rahul Verma
9876543210
rahul.verma.demo@outlook.com
rahul.verma.demo@outlook.com



""" 
    # Send email with attachment
    send_email(to_email, subject, body, resume_path)

print("Emails sent successfully.")

def main():
    print("-----AUTOMATION SCRITP FOR MAIL SENDER")

if __name__=="__main__":
    main()
