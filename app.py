from flask import Flask, request, jsonify
from database import db
from models.item import Item



app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secrect_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/diet-api'

db.init_app(app)

@app.route("/items", methods =["GET"])
def get_items():
    #pegando todos os registros da tabela
    items = Item.query.all()
    
    #retornando todos os registros em JSON
    try:
        return jsonify([item.serialize() for item in items]),200
    except:
        return jsonify({'message': 'Erro ao realizar busca.'}),500


if __name__ == "__main__":
    app.run(debug=True)