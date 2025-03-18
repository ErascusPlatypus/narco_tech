from flask import Flask, render_template, request, jsonify, send_file
import sqlite3
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

app = Flask(__name__)

# SQLite Database Setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  product TEXT,
                  amount TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'admin123':
        return jsonify({'success': True, 'message': 'Admin login successful!'})
    return jsonify({'success': False, 'message': 'Login failed. Try again.'})

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/transaction', methods=['POST'])
def transaction():
    data = request.get_json()
    product = data.get('product')
    amount = data.get('amount')
    timestamp = data.get('timestamp')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO transactions (product, amount, timestamp) VALUES (?, ?, ?)',
              (product, amount, timestamp))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Transaction successful! Receipt stored.'})

@app.route('/receipt')
def download_receipt():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions ORDER BY id DESC LIMIT 1')
    row = c.fetchone()
    conn.close()

    if not row:
        return "No transactions found", 404

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "NarcoTech Receipt")
    p.drawString(100, 730, f"Product: {row[1]}")
    p.drawString(100, 710, f"Amount: {row[2]}")
    p.drawString(100, 690, f"Date: {row[3]}")
    p.showPage()
    p.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='receipt.pdf', mimetype='application/pdf')

@app.route('/all-receipts')
def download_all_receipts():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions')
    rows = c.fetchall()
    conn.close()

    if not rows:
        return "No transactions found", 404

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "NarcoTech All Transactions")
    y = 730
    for row in rows:
        p.drawString(100, y, f"ID: {row[0]} | Product: {row[1]} | Amount: {row[2]} | Date: {row[3]}")
        y -= 20
        if y < 50:
            p.showPage()
            y = 750
    p.showPage()
    p.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='all-transactions.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True, port=5000)