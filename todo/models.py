from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    expected_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)


    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "<Todo {}>".format(self.text)
