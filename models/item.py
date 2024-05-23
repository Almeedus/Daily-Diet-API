from database import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True, )
    description = db.Column(db.String(80), default="None")
    dateTime = db.Column(db.DateTime, nullable=False)
    onDiet = db.Column(db.Boolean)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'dateTime': self.dateTime,
            'onDiet': self.onDiet
        }