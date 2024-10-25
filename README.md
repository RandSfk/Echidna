# Echidna
Echidna is an automated tool for creating Instagram accounts. It simplifies the process of generating new accounts by handling the registration process programmatically.

## Features
- Automatically creates new Instagram accounts.
- Customizable options for usernames, passwords, and other account details.
- Supports proxies to avoid IP rate limiting.
- Easy-to-use configuration for account generation.

## Requirements
- Python 3.8+
- Required Python libraries (see `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/echidna.git
   cd echidna
Install the required libraries:
bash
Salin kode
pip install -r requirements.txt
Usage
Configure the settings in config.json:

Set up your desired usernames, passwords, email domains, and proxies (if applicable).
Run the script:

bash
Salin kode
python echidna.py
Follow the on-screen instructions to monitor the account creation process.

Configuration
config.json:
Configure details such as usernames, email patterns, and proxies.
Example:
json
Salin kode
{
  "username_pattern": "user_####",
  "password": "yourpassword123",
  "email_domain": "@example.com",
  "use_proxies": true,
  "proxies": [
    "http://proxy1:port",
    "http://proxy2:port"
  ]
}
Notes
Instagram may have rate limits and anti-bot protections. Use proxies and handle captchas if needed.
Make sure to comply with Instagram's terms of service when using this tool.
Disclaimer
This tool is for educational purposes only. The user is responsible for any actions taken using this tool.

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
