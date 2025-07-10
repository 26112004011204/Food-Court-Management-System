# 🍽️ Food Court Management System

A command-line Python application for managing a food court. This system allows table bookings, food ordering, billing, and customer feedback, using file handling and dictionaries.

---

## 🧠 Features

- 🪑 Book and manage tables
- 📋 Display a rich Indian menu with prices
- 🧾 Take orders and calculate bills per table
- 🗂 Save order data to `orders.txt`
- 💬 Collect and store customer feedback in `feedback.txt`
- ✅ Simple, user-friendly terminal interface

---

## 📁 Project Structure

foodcourt/
├── foodcourt.py # Main CLI app logic
├── menu_items.py # Menu item dictionary with prices
├── orders.txt # Saved orders (auto-generated)
├── feedback.txt # Saved feedback (auto-generated)
└── README.md # Project description


---

## 🍛 Menu Preview

Here’s a sample of items from the menu:

| Item                        | Price (₹) |
|----------------------------|-----------|
| Samosa                     | 3.99      |
| Chicken Tikka              | 6.99      |
| Dal Makhani                | 8.99      |
| Butter Chicken             | 13.99     |
| Gulab Jamun                | 4.49      |
| Masala Chai                | 2.49      |
| Mango Lassi                | 3.99      |

✅ Full menu contains **30+ items** across Starters, Mains, Breads, Desserts, and Drinks.

---

## ▶️ How to Run

Run the program:
python foodcourt.py
Follow the on-screen options like:
Book a table
Order food
Calculate bill
Give feedback
File Outputs

orders.txt — stores each table’s order
feedback.txt — stores customer name + feedback
