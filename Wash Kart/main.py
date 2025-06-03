from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book-laundry', methods=['POST'])
def book_laundry():
    data = request.get_json()
    
    # Validate and process the data
    student_id = data.get('student_id')
    phone = data.get('phone')
    location = data.get('location')
    items = data.get('items')
    
    total_qty = sum(items.values())
    if total_qty > 20:
        return jsonify({'success': False, 'message': 'Cannot book more than 20 items'}), 400

    # TODO: Save to DB or perform logic here
    print("Booking received:")
    print(f"ID: {student_id}, Phone: {phone}, Location: {location}, Items: {items}")
    
    return jsonify({'success': True, 'message': 'Laundry booked successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
