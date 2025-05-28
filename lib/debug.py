from lib.models import session, init_db
from lib.helpers import *
from rich.console import Console

console = Console()

def debug():
    """Test your application during development"""
    init_db()
    
    # Test user creation
    user = create_user("testuser", "test@example.com")
    console.print(f"Created test user: {user}")
    
    # Test magazine creation
    magazine = create_magazine("Test Magazine", "This is a test magazine")
    console.print(f"Created test magazine: {magazine}")
    
    # Test issue creation
    issue = create_issue("Test Issue", magazine.id)
    console.print(f"Created test issue: {issue}")
    
    # Test article creation
    article = create_article("Test Article", "This is test content", user.id, issue.id)
    console.print(f"Created test article: {article}")
    
    # Test subscription
    subscription = create_subscription(user.id, magazine.id)
    console.print(f"Created test subscription: {subscription}")
    
    # Test queries
    console.print("\n[bold]All Users:[/bold]")
    for u in get_all_users():
        console.print(u)
    
    console.print("\n[bold]All Magazines:[/bold]")
    for m in get_all_magazines():
        console.print(m)
    
    console.print("\n[bold]All Articles:[/bold]")
    for a in get_all_articles():
        console.print(a)

if __name__ == '__main__':
    debug()