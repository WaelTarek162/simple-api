from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)

order = {
    "order1": {
        "size": "small",
        "Topping": "Cheese",
        "Crust": "Thin Crust"
    },
    "order2": {
        "size": "large",
        "Topping": "Cheese",
        "Crust": "Crust"
    }
}


@app.route('/')
def hello_world():
    return 'hello ppop'


@app.route('/order')
def get_order():
    return 'Choose your order'


@app.route('/order/<orderid>')
def get_order_details(orderid):
    if orderid in order:
        response = make_response(jsonify(order[orderid]), 200)
        return response
    return 'Order not found'


@app.route('/order/<orderid>/<item>')
def get_order_item(orderid, item):
    item = order[orderid].get(item)
    if item:
        response = make_response(jsonify(item), 200)
        return response
    return 'Order not found'


@app.route('/order/<orderid>', methods=["POST"])
def post_order_details(orderid):  ## create order
    req = request.get_json()
    if orderid in order:
        response = make_response(jsonify({"error": "order ID is already exists"}), 400)
        return response
    order.update({orderid: req})
    response = make_response(jsonify({"message": "New order created"}), 201)

    return response


@app.route('/order/<orderid>', methods=["PUT"])
def put_order_details(orderid):  ## put order
    req = request.get_json()
    if orderid in order:
        for k, v in req.items:
            order[orderid][k] = v
        order[orderid] = req
        response = make_response(jsonify({"message": "Order Updated"}), 200)
        return response
    order.update({orderid: req})
    response = make_response(jsonify({"message": "New order created"}), 201)

    return response


@app.route('/order/<orderid>', methods=["PATCH"])
def patch_order_details(orderid):  ## patch order
    req = request.get_json()
    if orderid in order:
        order[orderid] = req
        response = make_response(jsonify({"message": "Order Updated"}), 200)
        return response
    order.update({orderid: req})
    response = make_response(jsonify({"message": "New order created"}), 201)

    return response


@app.route('/order/<orderid>', methods=["DELETE"])
def delete_order_details(orderid):  ## delete order
    if orderid in order:
        del order[orderid]
        response = make_response(jsonify({"message": "Order deleted"}), 204)
        return response
    response = make_response(jsonify({"error": "order not found"}), 404)

    return response


if __name__ == '__main__':
    app.run(debug=True)
