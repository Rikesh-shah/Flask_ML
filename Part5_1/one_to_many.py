from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key = True)
    team = db.Column(db.String(50), nullable=False, unique=True)
    state = db.Column(db.String(50), nullable=False)
    members = db.relationship("Player", backref="team")  #it tells the sqlalchemy that team table is related to player table and backref creates an imaginary columnn named teams in the players table

    def __repr__(self):
        return f"Team('{self.team}', '{self.state}')"
    

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))

    def __repr__(self):
        return f"Team('{self.name}', '{self.nationality}')"
    

if __name__ == "__main__":
    app.run(debug=True)