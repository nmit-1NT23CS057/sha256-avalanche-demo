# 🔐 SHA-256 Hash & Avalanche Effect Visualizer

An interactive web application built using Streamlit to demonstrate SHA-256 hashing and the Avalanche Effect in cryptography.

---

## 📌 Overview

This project helps visualize how secure hash functions work, specifically SHA-256. It also demonstrates the **Avalanche Effect**, where even a tiny change in input leads to a completely different hash output.

---

## ✨ Features

* 🔤 Generate SHA-256 hash for text input
* 📁 Generate SHA-256 hash for uploaded files
* ⚡ Demonstrate Avalanche Effect for text inputs
* 📊 Compare hash differences for files with highlighted changes
* 📈 Similarity analysis between hashes

---

## 🧠 What is SHA-256?

SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that:

* Produces a fixed 256-bit output
* Is deterministic
* Is highly sensitive to input changes
* Is widely used in security applications like blockchain and password hashing

---

## ⚡ Avalanche Effect

A small change in input (even 1 character) causes a drastic change in the output hash.

Example:

```
Input 1: hello
Input 2: Hello

Hash outputs → Completely different
```

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎈
* hashlib (built-in library)

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/your-username/sha256-avalanche-demo.git
```

2. Navigate to the project folder:

```
cd sha256-avalanche-demo
```

3. Install dependencies:

```
pip install streamlit
```

4. Run the app:

```
streamlit run app.py
```

---

## 📂 Project Structure

```
├── app.py
├── README.md
```

---

## 🎯 Use Cases

* Learning cryptography fundamentals
* Demonstrating hashing concepts in classrooms
* Interview/project showcase
* Understanding data integrity mechanisms

---
