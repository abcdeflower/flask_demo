# coding:utf-8
from app import db
from log.logger import ErrorLogger


class Base:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            ErrorLogger.error(e)
            db.session.rollback()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            ErrorLogger.error(e)
            db.session.rollback()

    def update(self, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            ErrorLogger.error(e)
            db.session.rollback()


class User(Base, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(127), nullable=False)

    def __repr__(self):
        return self.id
