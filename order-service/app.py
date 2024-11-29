from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/order', methods=['POST'])
def create_order():
    order_data = request.json
    orders.append(order_data)
    return jsonify({"message": "Order created successfully!"}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

