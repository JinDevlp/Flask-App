from .import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique = True )
    first_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime(timezone=True),default=func.now())
    project_owned = db.relationship('Project' ,backref='user') 
    # current_projects = projects that this user is part of


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False, unique = True)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    members = db.relationship('User', secondary='current_projects',lazy='subquery',backref=db.backref('users',lazy=True), cascade="all")

members_in_project = db.Table('members_in_project',
                              db.Column('project_id',db.Integer,db.ForeignKey('project.id'),primary_key=True),
                              db.Column('user_id',db.Integer,db.ForeignKey('user.id'),primary_key=True)
                              )
