from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book-laundry', methods=['POST'])
def book_laundry():
    data = request.get_json()

    # Extract and validate data
    student_id = data.get('student_id')
    phone = data.get('phone')
    location = data.get('location')
    items = data.get('items')

    total_qty = sum(items.values())
    if total_qty > 20:
        return jsonify({'success': False, 'message': 'Cannot book more than 20 items'}), 400

    # Simulate saving to database (for now just print)
    print("Booking received:")
    print(f"ID: {student_id}, Phone: {phone}, Location: {location}, Items: {items}")

    return jsonify({'success': True, 'message': 'Laundry booked successfully!'})

# This is the key part to work on Render
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Render sets PORT env var
    app.run(host='0.0.0.0', port=port)
