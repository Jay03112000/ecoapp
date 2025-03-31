# 🌍 ECOearth – Sustainable E-commerce Web Application

**ECOearth** is a fully functional e-commerce website designed to promote eco-friendly and sustainable products. Developed with the Django framework, this project features a robust shop system, user accounts, order management, contact form, and integrated blog — all styled with modern responsive front-end design.

---

## 🚀 Features

- 🛒 **E-commerce Storefront** – Display eco-products dynamically
- 👤 **User Authentication** – Register, login, and manage accounts
- 📦 **Order Checkout System** – Place and track orders
- ✉️ **Contact Form with Email Support** – Integrated email service for customer queries
- 📝 **Blog Section** – Stay updated with eco-conscious news and articles
- 📅 **Events Page** – Promote local and global green initiatives
- 📱 **Responsive Design** – Mobile and tablet friendly layout

---

## 🗂️ Project Structure

```
ECOearth/
│
├── accounts/              # User registration, login, profile
├── blog/                  # Blog pages and articles
├── contact/               # Contact form with email support
├── ecoearth/              # Main project settings and configurations
├── events/                # Events and eco-awareness activities
├── orders/                # Checkout, order summary, and payment
├── store/                 # Core shopping functionality
├── static/                # Static files (CSS, JS, images, fonts)
├── templates/             # HTML templates (shop.html, index.html, etc.)
├── webfonts/, css/, js/   # Frontend assets (Bootstrap, JS logic, fonts)
├── db.sqlite3             # SQLite database file
├── manage.py              # Django management script
├── index.html             # Entry point for home page
├── shop.html              # Dynamic product display page
└── README.md              # You're here!
```

---

## 🧰 Technologies Used

- 🌐 **Framework**: Django (Python)
- 🎨 **Frontend**: HTML5, CSS3, Bootstrap
- ⚙️ **Backend**: SQLite3, Django ORM
- 📬 **Email Service**: Configured via `settings.py`
- 📱 **Responsive Design**: Mobile-ready UI components

---

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ECOearth.git
cd ECOearth
```

### 2. Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser 🚀

---

## 📌 Screenshots & Pages

- **🏠 Home Page** – index.html
- **🛍️ Shop Page** – shop.html with dynamic eco-product listings
- **✉️ Contact Form** – connected with email services
- **📖 Blog & Events** – informative sections for engagement

> Images, logos, and other assets are inside the `static/` folder and integrated via Bootstrap.

---

## 🧠 Ideal For

- Portfolio showcase in full-stack development
- Learning Django and e-commerce architecture
- Promoting eco-conscious product ideas 🌱

---

## 👨‍💻 Developed By

Jay Patel
---

## ⭐ Support & Share

If you like this project, give it a ⭐ on GitHub and share it with fellow devs and sustainability enthusiasts!

