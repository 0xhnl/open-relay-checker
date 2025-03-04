# Open Relay Checker

This is a simple Python script to test email sending functionality via an SMTP server. It allows you to specify the sender, recipient, and mail server as command-line arguments, making it easy to verify your mail server configuration.

# Usage

- You need to verify with nuclei template:

```bash
➜  ~ nuclei -t open-relay.yaml -u webmail.test.com                                   

                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v3.3.9

		projectdiscovery.io

[INF] Current nuclei version: v3.3.9 (latest)
[INF] Current nuclei-templates version: v10.1.3 (latest)
[WRN] Scan results upload to cloud is disabled.
[INF] New templates added in latest release: 52
[INF] Templates loaded for current scan: 1
[WRN] Loading 1 unsigned templates for scan. Use with caution.
[INF] Targets loaded for current scan: 1
[smtp-open-relay] [tcp] [high] webmail.test.com:25
```

- Send the email like that:

```bash
python3 send.py -s <sender_email> -r <recipient_email> -u <mail_server>
```

# Freatures

- Sends a customizable test email.
- Supports dynamic input for sender, recipient, and mail server.
- Includes error handling for SMTP and other exceptions.
