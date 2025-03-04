import smtplib
import argparse

# Define the default values for port and email content
PORT = 25  # Default SMTP port

# Updated Subject and Email Body
SUBJECT = "System Notification: Test Email"
EMAIL_BODY = """Dear Support Team,

This is a system-generated test email to verify the functionality of the mail server. 
Please disregard this message if received in error.

Thank you for your attention.

Best regards,
wkwkwkwkwkwk
"""

def send_email(mail_server, sender_email, recipient_email):
    # Construct the email message
    email_message = f"""From: {sender_email}
To: {recipient_email}
Subject: {SUBJECT}

{EMAIL_BODY}
"""

    try:
        # Connect to the mail server
        print(f"Connecting to mail server {mail_server} on port {PORT}...")
        with smtplib.SMTP(mail_server, PORT) as server:
            # Start the conversation
            server.ehlo()

            # Send the email
            print("Sending email...")
            server.sendmail(sender_email, recipient_email, email_message)

            # Confirm success
            print("Email sent successfully!")

    except smtplib.SMTPException as e:
        # Handle errors related to SMTP
        print(f"An error occurred while sending the email: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Send a test email using an SMTP server.")
    
    # Add arguments for sender, recipient, and mail server
    parser.add_argument('-s', '--sender', required=True, help='Sender email address (e.g., attacker@test.com)o')
    parser.add_argument('-r', '--recipient', required=True, help='Recipient email address (e.g., victim@test.com)')
    parser.add_argument('-u', '--server', required=True, help='Mail server URL (e.g., webmail.test.com)')
    
    # Parse the arguments
    args = parser.parse_args()

    # Extract values from arguments
    MAIL_SERVER = args.server
    SENDER_EMAIL = args.sender
    RECIPIENT_EMAIL = args.recipient

    # Call the function to send the email
    send_email(MAIL_SERVER, SENDER_EMAIL, RECIPIENT_EMAIL)
