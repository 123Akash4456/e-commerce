from flask import Flask, request, render_template 
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient('mongodb+srv://Akash_001:12345@cluster0.vcrqce4.mongodb.net/')
db = client['mydata']
items = db['items']

@app.route('/')
def list_items():
    items_list = items.find()
    return render_template('list_items.html', items=items_list)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))
        discount = float(request.form.get('discount'))
        items.insert_one({'name': name, 'price': price, 'discount': discount})
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)