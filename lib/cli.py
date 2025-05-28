import click 
from rich.console import Console
from rich.table import Table
from lib.helpers import *
from lib.models import init_db

console = Console()

@click.group()
def cli():
    """Magazine Publication CLI"""
    pass

@cli.command()
def init():
    """Initialize the database"""
    init_db()
    console.print("[green]Database initialized successfully![/green]")

# User commands
@cli.group()
def user():
    """Manage users"""
    pass

@user.command()
@click.option('--username', prompt=True)
@click.option('--email', prompt=True)
def create(username, email):
    """Create a new user"""
    user = create_user(username, email)
    console.print(f"[green]Created user: {user.username}[/green]")

@user.command()
def list():
    """List all users"""
    users = get_all_users()
    table = Table(title="Users")
    table.add_column("ID", style="cyan")
    table.add_column("Username")
    table.add_column("Email")
    
    for user in users:
        table.add_row(str(user.id), user.username, user.email)
    
    console.print(table)

# Magazine commands
@cli.group()
def magazine():
    """Manage magazines"""
    pass

@magazine.command()
@click.option('--title', prompt=True)
@click.option('--description', prompt=True)
def create(title, description):
    """Create a new magazine"""
    magazine = create_magazine(title, description)
    console.print(f"[green]Created magazine: {magazine.title}[/green]")

@magazine.command()
def list():
    """List all magazines"""
    magazines = get_all_magazines()
    table = Table(title="Magazines")
    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Description")
    
    for magazine in magazines:
        desc = magazine.description[:50] + "..." if len(magazine.description) > 50 else magazine.description
        table.add_row(str(magazine.id), magazine.title, desc)
    
    console.print(table)

# Issue commands
@cli.group()
def issue():
    """Manage issues"""
    pass

@issue.command()
@click.option('--title', prompt=True)
@click.option('--magazine-id', prompt=True, type=int)
def create(title, magazine_id):
    """Create a new issue"""
    issue = create_issue(title, magazine_id)
    console.print(f"[green]Created issue: {issue.title}[/green]")

@issue.command()
@click.option('--magazine-id', required=False, type=int)
def list(magazine_id):
    """List issues (optionally by magazine)"""
    if magazine_id:
        issues = get_issues_by_magazine(magazine_id)
        title = f"Issues for Magazine ID {magazine_id}"
    else:
        issues = get_all_issues()
        title = "All Issues"
    
    table = Table(title=title)
    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Magazine")
    table.add_column("Publication Date")
    
    for issue in issues:
        table.add_row(
            str(issue.id),
            issue.title,
            issue.magazine.title,
            issue.publication_date.strftime("%Y-%m-%d")
        )
    
    console.print(table)

# Article commands
@cli.group()
def article():
    """Manage articles"""
    pass

@article.command()
@click.option('--title', prompt=True)
@click.option('--content', prompt=True)
@click.option('--author-id', prompt=True, type=int)
@click.option('--issue-id', prompt=True, type=int)
def create(title, content, author_id, issue_id):
    """Create a new article"""
    article = create_article(title, content, author_id, issue_id)
    console.print(f"[green]Created article: {article.title}[/green]")

@article.command()
@click.option('--author-id', required=False, type=int)
@click.option('--issue-id', required=False, type=int)
def list(author_id, issue_id):
    """List articles (optionally by author or issue)"""
    if author_id:
        articles = get_articles_by_author(author_id)
        title = f"Articles by Author ID {author_id}"
    elif issue_id:
        articles = get_articles_by_issue(issue_id)
        title = f"Articles in Issue ID {issue_id}"
    else:
        articles = get_all_articles()
        title = "All Articles"
    
    table = Table(title=title)
    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("Issue")
    table.add_column("Created At")
    
    for article in articles:
        table.add_row(
            str(article.id),
            article.title,
            article.author.username,
            f"{article.issue.magazine.title} - {article.issue.title}",
            article.created_at.strftime("%Y-%m-%d")
        )
    
    console.print(table)

# Subscription commands
@cli.group()
def subscription():
    """Manage subscriptions"""
    pass

@subscription.command()
@click.option('--user-id', prompt=True, type=int)
@click.option('--magazine-id', prompt=True, type=int)
@click.option('--duration', default=1, type=int)
def create(user_id, magazine_id, duration):
    """Create a new subscription"""
    subscription = create_subscription(user_id, magazine_id, duration)
    console.print(f"[green]Created subscription for {duration} month(s)[/green]")

@subscription.command()
@click.option('--user-id', required=False, type=int)
@click.option('--magazine-id', required=False, type=int)
def list(user_id, magazine_id):
    """List subscriptions (optionally by user or magazine)"""
    if user_id:
        subscriptions = get_user_subscriptions(user_id)
        title = f"Subscriptions for User ID {user_id}"
    elif magazine_id:
        subscriptions = get_magazine_subscribers(magazine_id)
        title = f"Subscribers for Magazine ID {magazine_id}"
    else:
        subscriptions = get_all_subscriptions()
        title = "All Subscriptions"
    
    table = Table(title=title)
    table.add_column("ID", style="cyan")
    table.add_column("User")
    table.add_column("Magazine")
    table.add_column("Start Date")
    table.add_column("End Date")
    
    for sub in subscriptions:
        table.add_row(
            str(sub.id),
            sub.user.username,
            sub.magazine.title,
            sub.start_date.strftime("%Y-%m-%d"),
            sub.end_date.strftime("%Y-%m-%d") if sub.end_date else "N/A"
        )
    
    console.print(table)

if __name__ == '__main__':
    cli()