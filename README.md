# 🛡️ Strongest Password Manager (Cloud-Native)

An interactive, secure password generation and storage solution built with **Python**, **SQLAlchemy**, and **Streamlit**, integrated with a **Cloud-hosted PostgreSQL** database.

---

## 🚀 Live Demo
**[Click here to access the live website](https://passwordgeneratorapp-kncjx2vc9dz6y6qjbsgtbx.streamlit.app/)**

---

## 📽️ App Preview
![Password Manager Demo](https://github.com/Ahmedkamalhikal/password_generator_app/blob/main/PWGEN.gif?raw=true)

---

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Web-based interactive UI)
* **Database ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database:** [Aiven PostgreSQL](https://aiven.io/) (Managed Cloud Database)
* **Language:** Python 3.12+
* **Deployment:** Streamlit Community Cloud

---

## ✨ Key Features
* **Dynamic Password Generation:** Uses custom logic to ensure passwords meet high complexity standards (Uppercase, Lowercase, Digits, and Symbols).
* **Cloud Persistence:** Securely saves credentials to an online PostgreSQL instance on Aiven.
* **Relational Mapping:** Implemented using SQLAlchemy Models for clean and maintainable database interactions.
* **Secure Retrieval:** Built-in search functionality to fetch credentials by website name.
* **Responsive Layout:** Clean UI with side-by-side controls and tabbed navigation.

---

## 🏗️ Architecture
The app follows a modern web architecture:
1.  **UI Layer:** Streamlit captures user inputs and triggers events.
2.  **Logic Layer:** Python functions handle cryptographic-grade random generation.
3.  **Data Layer:** SQLAlchemy translates Python objects into SQL commands.
4.  **Cloud Layer:** Aiven manages the physical storage and security (SSL/TLS).

---

## 🔒 Security Best Practices
* **Secrets Management:** Sensitive database credentials are never hard-coded. They are managed via **Streamlit Secrets** (`st.secrets`).
* **Environment Dialects:** Automatically handles `postgres://` to `postgresql://` conversion for driver compatibility.
* **Defensive Programming:** Implemented `try-except` blocks with automatic `session.rollback()` to maintain database integrity during errors.

---

## 📖 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/Ahmedkamalhikal/password_generator_app.git](https://github.com/Ahmedkamalhikal/password_generator_app.git)
