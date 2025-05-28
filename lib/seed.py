from faker import Faker
from lib.helpers import *
from lib.models import session
import random
from datetime import datetime, timedelta

fake = Faker()

def seed_database():
    # Clear existing data
    session.query(Subscription).delete()
    session.query(Article).delete()
    session.query(Issue).delete()
    session.query(Magazine).delete()
    session.query(User).delete()
    session.commit()

    # Create users
    users = []
    for _ in range(10):
        user = create_user(
            username=fake.unique.user_name(),
            email=fake.unique.email()
        )
        users.append(user)
    
    # Create magazines
    magazines = []
    for _ in range(5):
        magazine = create_magazine(
            title=fake.catch_phrase(),
            description=fake.paragraph()
        )
        magazines.append(magazine)
    
    # Create issues for each magazine
    issues = []
    for magazine in magazines:
        for _ in range(random.randint(2, 5)):
            issue = create_issue(
                title=f"Vol. {random.randint(1, 10)} No. {random.randint(1, 12)}",
                magazine_id=magazine.id
            )
            issues.append(issue)
    
    # Create articles for each issue
    for issue in issues:
        for _ in range(random.randint(3, 8)):
            create_article(
                title=fake.sentence(),
                content=fake.text(max_nb_chars=1000),
                author_id=random.choice(users).id,
                issue_id=issue.id
            )
    
    # Create subscriptions
    for user in users:
        subscribed_magazines = random.sample(magazines, random.randint(1, 3))
        for magazine in subscribed_magazines:
            create_subscription(
                user_id=user.id,
                magazine_id=magazine.id,
                duration_months=random.randint(1, 12)
            )
    
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()