from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum

db = SQLAlchemy()


class UserRole(Enum):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

class Status(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'
    COMPLETED = 'completed'

class RequestStatus(Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    NEGOTIATING = 'negotiating'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.USER.value)


    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'
    


class Influencer(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), )
    niche = db.Column(db.String(100), )
    reach = db.Column(db.Integer, )
    profile_public = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    user = db.relationship('User', backref=db.backref( 'influencers', lazy=True))


class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), )
    budget = db.Column(db.Integer, )
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    user = db.relationship('User', backref=db.backref('sponsors', lazy=True))


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(100), nullable=False, default=Status.PENDING.value)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    sponsor = db.relationship('Sponsor', backref=db.backref('campaigns', lazy=True))
    influencer = db.relationship('Influencer', backref=db.backref('campaigns', lazy=True))


class AdRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'), nullable=False)
    status = db.Column(db.String(100), nullable=False, default=RequestStatus.PENDING.value)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    campaign = db.relationship('Campaign', backref=db.backref('ad_requests', lazy=True))
    influencer = db.relationship('Influencer', backref=db.backref('ad_requests', lazy=True))

    
class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    # updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    user = db.relationship('User', backref=db.backref('logs', lazy=True))
