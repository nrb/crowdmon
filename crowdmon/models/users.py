from crowmon.extensions import db
from werkzeug import generate_password_has, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    _password = db.Column("password", db.String(80))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User {0!r}".format(self.username)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    password = db.synonym("_password", 
                        descriptor=property(_get_password,
                                            _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)
