WEB SCRAPING AND PRICE MONITORING APP

A Python-based desktop application that lets users monitor product prices on **Amazon** and **Flipkart**, filter results based on their budget, and receive **email alerts** for the best deals — all using web scraping, automation, and scheduling.

---

## ✅ Features

- 🌐 **Scrapes product listings** from Amazon (Flipkart integration can be added similarly)
- 💸 Filters products under **user-defined budget**
- ⏱️ Automatically **runs for a user-specified duration** (e.g., 10 minutes)
- 📧 Sends an **email** with the best deals found
- 💾 Saves scraped data to `product_prices.csv`
- 🖥️ Simple GUI using `Tkinter`

---

## 🛠️ Tech Stack

- `Python`
- `Selenium` – for browser automation
- `webdriver-manager` – manages browser drivers
- `Tkinter` – GUI for user input
- `Pandas` – for data handling
- `smtplib` – to send emails
- `schedule` *(optional)* – for periodic checks (if used)

---

## 📂 Project Structure

```
📁 price-monitor-app/
├── amazon.py           # Scrapes Amazon product data
├── gui.py              # GUI for user inputs
├── main.py             # Orchestrates monitoring and filtering
├── utils.py            # Email sending and CSV saving
├── requirements.txt    # Dependencies
└── product_prices.csv  # Output (auto-generated)
```

---

## 🧑‍💻 How It Works

1. User launches the app using `gui.py`
2. Enters:
   - Product name (e.g., "iPhone")
   - Budget (e.g., ₹60,000)
   - Duration (e.g., 10 minutes)
3. Script searches Amazon for the product periodically
4. Filters results under budget
5. Sends email with matching deals
6. Saves results in `product_prices.csv`

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/price-monitor-app.git
cd price-monitor-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python gui.py
```

---

## 📧 Email Setup

In `utils.py`, replace with your actual Gmail credentials (use an **App Password**):

```python
sender = "your_email@gmail.com"
receiver = "your_email@gmail.com"
password = "your_app_password"  # NOT your regular Gmail password
```

Enable "Less secure apps" or use App Password from Google account settings.

---

## 📦 `requirements.txt`

```
selenium
webdriver-manager
pandas
```

Add `schedule` if you're scheduling repeated runs.

---

## 📝 Future Improvements

- ✅ Add Flipkart scraping in a new `flipkart.py`
- 💾 Store results in SQLite or MongoDB
- 📱 Build mobile-friendly UI with Flask + HTML
- 📈 Add graphs for price trends

---

## 🛡️ Disclaimer

This app is intended for educational purposes. Frequent scraping may violate website terms of service. Use responsibly.

---

## 🙌 Author

**Vishwa Vardhini**  
[LinkedIn](#) | [Email](mailto:vishwavardhinidumpeti@gmail.com)

---
