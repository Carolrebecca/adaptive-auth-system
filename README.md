# 🔐 Adaptive Authentication System (Cyber Range Simulation)

## 📌 Overview

This project is a **Cyber Range-based Attack–Defense Simulation System** developed using Flask. It demonstrates how insecure authentication systems can be exploited and how modern security mechanisms prevent such attacks.

The system provides a **real-time interactive dashboard** with attack simulation, secure login mechanisms, and live monitoring.

---

## 🎯 Objectives

* Simulate password-based attacks (dictionary attack)
* Demonstrate insecure vs secure authentication
* Implement multi-layer defense mechanisms
* Provide real-time monitoring using logs and analytics

---

## ⚙️ Features

### 🔓 Insecure Authentication

* Plain-text password validation
* Vulnerable to brute-force and dictionary attacks

### 🔐 Secure Authentication

* SHA-256 password hashing
* Account lock after multiple failed attempts
* OTP-based second layer authentication

### 🧨 Attack Simulation

* Dictionary attack simulation
* Real-time attack progress visualization
* Password cracking demonstration

### 📊 Dashboard & Monitoring

* Live logs with attack and login activity
* Real-time statistics (attacks, failures)
* Interactive charts (line + doughnut)

### 🎨 UI/UX

* Glassmorphism + neon cyber UI
* Animated dashboard
* Progress bars and interactive feedback

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Chart.js
* **Security:** Hashlib (SHA-256)

---

## 📂 Project Structure

```
project/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## 🚀 How to Run Locally

1. Install dependencies:

```
pip install flask
```

2. Run the app:

```
python app.py
```

3. Open browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

The application can be deployed using platforms like:

* Render
* Heroku (alternative)

---

## 🧠 Key Concepts Demonstrated

* Cyber Range Simulation
* Authentication Security
* Password Cracking Techniques
* Multi-Factor Authentication (MFA)
* Intrusion Detection (basic logging)

---

## 📈 Future Enhancements

* CAPTCHA integration
* Role-Based Access Control (RBAC)
* Machine Learning-based anomaly detection
* Database integration (SQLite/MySQL)

---

## 👩‍💻 Author

Carol Rebecca

---

## 📜 License

This project is for academic and educational purposes only.
