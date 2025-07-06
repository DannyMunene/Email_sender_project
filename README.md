# Email Sender

A simple project to send emails using Python.

## 📧 Features

- Send emails to one or multiple recipients
- Supports plain text or HTML content
- Custom subject lines and attachments
- SMTP server configuration

## 🚀 Technologies Used

- Python
- `smtplib`
- `email` package
- (Optional) Flask or other framework if applicable

## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/dannymunene/email-sender.git
   cd email-sender
Install any required packages (if needed):

bash

pip install -r requirements.txt
Configure your SMTP settings in a .env or config file:

ini

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_password
Run the script:

bash

python send_email.py
⚠️ Notes

Make sure to enable "less secure app access" or use an app password if using Gmail.

Avoid hardcoding sensitive information.

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Created by Danny Munene
