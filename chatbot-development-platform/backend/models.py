from .app import db

class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_text = db.Column(db.String(255), nullable=False)
    response_text = db.Column(db.String(255), nullable=False)
