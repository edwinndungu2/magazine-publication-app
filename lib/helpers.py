from lib.models import session
from lib.models import User, Magazine, Issue, Article, Subscription
from datetime import datetime, timedelta

# User CRUD operations
def create_user(username, email):
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    return user

def get_all_users():
    return session.query(User).all()

def find_user_by_id(user_id):
    return session.query(User).filter_by(id=user_id).first()

def update_user(user_id, username=None, email=None):
    user = find_user_by_id(user_id)
    if user:
        if username:
            user.username = username
        if email:
            user.email = email
        session.commit()
    return user

def delete_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

# Magazine CRUD operations
def create_magazine(title, description):
    magazine = Magazine(title=title, description=description)
    session.add(magazine)
    session.commit()
    return magazine

def get_all_magazines():
    return session.query(Magazine).all()

def find_magazine_by_id(magazine_id):
    return session.query(Magazine).filter_by(id=magazine_id).first()

def update_magazine(magazine_id, title=None, description=None):
    magazine = find_magazine_by_id(magazine_id)
    if magazine:
        if title:
            magazine.title = title
        if description:
            magazine.description = description
        session.commit()
    return magazine

def delete_magazine(magazine_id):
    magazine = find_magazine_by_id(magazine_id)
    if magazine:
        session.delete(magazine)
        session.commit()
        return True
    return False

# Issue CRUD operations
def create_issue(title, magazine_id):
    issue = Issue(title=title, magazine_id=magazine_id)
    session.add(issue)
    session.commit()
    return issue

def get_all_issues():
    return session.query(Issue).all()

def find_issue_by_id(issue_id):
    return session.query(Issue).filter_by(id=issue_id).first()

def get_issues_by_magazine(magazine_id):
    return session.query(Issue).filter_by(magazine_id=magazine_id).all()

# Article CRUD operations
def create_article(title, content, author_id, issue_id):
    article = Article(title=title, content=content, author_id=author_id, issue_id=issue_id)
    session.add(article)
    session.commit()
    return article

def get_all_articles():
    return session.query(Article).all()

def find_article_by_id(article_id):
    return session.query(Article).filter_by(id=article_id).first()

def get_articles_by_author(author_id):
    return session.query(Article).filter_by(author_id=author_id).all()

def get_articles_by_issue(issue_id):
    return session.query(Article).filter_by(issue_id=issue_id).all()

# Subscription CRUD operations
def create_subscription(user_id, magazine_id, duration_months=1):
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=30*duration_months)
    
    subscription = Subscription(
        user_id=user_id,
        magazine_id=magazine_id,
        start_date=start_date,
        end_date=end_date
    )
    session.add(subscription)
    session.commit()
    return subscription

def get_all_subscriptions():
    return session.query(Subscription).all()

def find_subscription_by_id(subscription_id):
    return session.query(Subscription).filter_by(id=subscription_id).first()

def get_user_subscriptions(user_id):
    return session.query(Subscription).filter_by(user_id=user_id).all()

def get_magazine_subscribers(magazine_id):
    return session.query(Subscription).filter_by(magazine_id=magazine_id).all()