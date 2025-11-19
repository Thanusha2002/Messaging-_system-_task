# 📩 Messaging System with RabbitMQ, Celery, Nginx, and Python

A simple messaging system demonstrating **asynchronous task processing** using **RabbitMQ**, **Celery**, and **Python**, exposed to the internet via **ngrok** and served through **Nginx**.

This project allows users to:

* **Send an email asynchronously** using Celery workers.
* **Log the current server time** through a simple API endpoint.

---

## 🚀 1. Objective

The goal of this project is to show how background tasks work using a message broker (**RabbitMQ**) and a task queue (**Celery**). A lightweight Python web application exposes API endpoints that trigger asynchronous tasks. The entire service is reverse-proxied through **Nginx** and made publicly accessible using **ngrok**.

---

## 🧱 2. System Architecture

### **🔹 Nginx (Frontend)**

* Runs on **port 80**.
* Acts as a **reverse proxy**.
* Forwards requests to the Python backend (Gunicorn/Uvicorn).

### **🔹 Python Application (Backend)**

* Built with **Flask** or **FastAPI**.
* Exposes the `/action` endpoint:

  * `?sendmail=<email>` → triggers async email-sending task.
  * `?talktome` → logs current timestamp.

### **🔹 Celery + RabbitMQ (Task Queue)**

* **RabbitMQ** → message broker.
* **Celery workers** → execute tasks in the background:

  * Sending email (`send_email_task`)
  * Logging time (`log_time_task`)

### **🔹 Ngrok (Public Exposure)**

* Tunnels local Nginx to a **public HTTPS URL**.
* Enables external testing of API endpoints.

---

## ⚙️ 3. Functional Requirements

### **📧 Email Sending — `/action?sendmail=<email>`**

* Accepts a recipient email ID.
* Publishes a Celery task.
* Worker sends the email using SMTP.

### **🕒 Logging Time — `/action?talktome`**

* Writes the current timestamp to `app.log`.
* Demonstrates simple request handling (can also be Celery-based).

### **🛠 Task Execution**

* Email sending → **asynchronous**.
* Time logging → **synchronous** (or optional Celery task).

---

## 🛠️ 4. Implementation Steps

### **1. Install Dependencies**

* RabbitMQ
* Celery
* Flask/FastAPI
* Gunicorn/Uvicorn
* Nginx
* Ngrok

### **2. Start RabbitMQ**

```bash
sudo service rabbitmq-server start
```

### **3. Configure Celery**

* Define Celery app and tasks (email + logging).

### **4. Build Python Backend**

* Create `/action` route.
* Handle `sendmail` and `talktome` query parameters.
* Connect Celery tasks.

### **5. Configure Email SMTP**

* Use Gmail SMTP or any SMTP provider.
* Store credentials in environment variables.

### **6. Run Application Behind Nginx**

* Nginx → Gunicorn/Uvicorn → Flask/FastAPI → Celery → RabbitMQ

### **7. Start Ngrok**

```bash
ngrok http 80
```

Use the HTTPS URL for external testing.

---

## 🧪 5. Testing the System

### **Send Email**

```
https://<ngrok-id>.ngrok-free.dev/action?sendmail=test@example.com
```

Expected: Email is delivered asynchronously.

### **Log Time**

```
https://<ngrok-id>.ngrok-free.dev/action?talktome=1
```

Expected: Timestamp is appended to `app.log`.

---

## 🎥 6. Deliverables

Your final submission includes:

* Fully working system accessible via ngrok.
* **Screen recording (≤3 minutes)** showing:

  * RabbitMQ running
  * Celery workers picking tasks
  * Flask app routing via Nginx
  * Email being sent
  * Log file updating
  * ngrok public endpoint testing

---

## 🛠 7. Technologies Used

* **RabbitMQ** — Message Broker
* **Celery** — Task Queue Manager
* **Flask / FastAPI** — Web Framework
* **Gunicorn / Uvicorn** — Application Server
* **Nginx** — Reverse Proxy
* **SMTP (Gmail)** — Email Sending
* **Ngrok** — Public Exposure
* **Python 3.9+**

---

## ✅ 8. Conclusion

This project demonstrates a production-like architecture using:

* Reverse proxying (Nginx)
* Background task execution (Celery + RabbitMQ)
* SMTP email automation
* Public API access via ngrok


Just tell me!
