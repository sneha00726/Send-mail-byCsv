# Send-mail-byCsv
Email Automation Script (Python)

Overview

This project is a Python-based automation script that sends emails with attachments (such as resumes) to multiple recipients using data from a CSV file. It is especially useful for job applications where you want to send emails to multiple HRs or recruiters efficiently.

Features:
Send emails to multiple recipients automatically
Read recipient data from a CSV file
Attach files (e.g., resume PDF)
Customizable email subject and body
Supports Gmail SMTP with secure login

Technologies Used:
Python
CSV module
smtplib (SMTP protocol)
email.mime (for email formatting and attachments)

How It Works:
Reads all contacts from the CSV file
Loops through each contact
Sends an email with subject, body, and attachment
Repeats for all recipients

License

This project is for educational purposes.
