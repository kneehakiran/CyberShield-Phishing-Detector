# 🔐 Phishing URL Detector

🔴 Live Demo: https://cybershield-phishing-detector.onrender.com

A Flask-based cybersecurity web application that detects potentially suspicious URLs using multiple phishing detection rules.

## 🚀 Features

* Detects URLs containing `@` symbols
* Detects excessively long URLs
* Detects suspicious keywords such as:

  * login
  * verify
  * bank
* Detects URLs with excessive subdomains
* Real-time detection through a web interface
* Dark-themed user interface

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS

## 📸 Project Preview

Enter a URL and instantly receive a phishing risk assessment.

## 📂 Project Structure

```text
app.py
README.md
```

## ▶️ Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install Flask

```bash
pip install flask
```

3. Run the application

```bash
python app.py
```

4. Open your browser

```text
http://127.0.0.1:5000
```

## 🔍 Detection Rules

The application flags URLs as suspicious when they:

* Contain `@`
* Contain phishing-related keywords
* Exceed a safe length threshold
* Have excessive subdomains

## 🎯 Future Improvements

* Machine Learning based detection
* URL reputation checking
* VirusTotal API integration
* Domain age verification
* Advanced threat scoring system

## 👨‍💻 Author

Neeha Kiran
Aspiring Cybersecurity Professional | Python Developer

```
```
