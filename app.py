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
    if items:
        return jsonify([item.serialize() for item in items]), 200
    else:
        return jsonify({'message': 'Erro ao realizar busca.'}), 500


@app.route("/items/<int:id>", methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    
    if item:
        return jsonify(item.serialize()), 200
    else:
        return jsonify({"message": "Item não encontrado"}), 404
    
    
@app.route("/items/<int:id>", methods=['PUT'])
def update_item(id):
    data = request.json
    item = Item.query.get(id)
    
    if item:
        item.name = data.get("name")
        item.description = data.get("description")
        item.dateTime = data.get("dateTime")
        item.onDiet = data.get("onDiet")
        
        db.session.commit()
        return jsonify({"message": "Item atualizado com sucesso"}), 200
    
    else:
        return jsonify({"message": "Item não encontrado"}), 404


@app.route("/items/new", methods=["POST"])
def new_item():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    dateTime = data.get('dateTime')
    onDiet = data.get('onDiet')
    item = None
    
    if name:
        item = Item(name=name,
                description=description,
                dateTime=dateTime,
                onDiet=onDiet)
        
        db.session.add(item)
        db.session.commit()
        return jsonify({"message":"Refeição criada com sucesso"}), 200

    return jsonify({"message":"Dados inválidos"}), 400


@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get(id)
    
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item deletado com sucesso"}), 200
    
    return jsonify({"message": "Item não encontrado"}), 404 

if __name__ == "__main__":
    app.run(debug=True)