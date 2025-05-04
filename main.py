from sqlite3_handler import SqlHandler
import click

sql_handler = SqlHandler("passwords.db")


@click.group()
def cli():
    pass


@cli.command()
@click.argument('website')
@click.option('-u', type=str, default=None)
def fn_pwd(website, u):
    if u is None:
        u = "NULL"
    query = f'SELECT password FROM passwords WHERE website = "{website}" AND username = "{u}";'
    password = sql_handler.execute(query)
    if password == []:
        print("no password found")
    else:
        print(password[0][0])


@cli.command()
@click.argument('website')
@click.argument('password')
@click.option('-u', type=str, default=None)
def en_pwd(website, password, u):
    query = f'SELECT password FROM passwords WHERE website = "{website}" AND username = "{u}";'
    passwords_found = sql_handler.execute(query)
    if u is None:
        u = "NULL"
    if passwords_found != []:
        print("Entry already exists with this website. To replace it, first delete that entry.")
    else:
        sql_handler.insert_password(website, password, u)


@cli.command()
@click.argument('website')
@click.option('-u', type=str, default=None)
def delete(website, u):
    username = u
    if username is None:
        username = 'NULL'
    elif website[0] == '@':
        website = website.replace('@', '')
        website = website + ' ' + username
        username = 'NULL'
    sql_handler.delete_password(website, username)

@cli.command()
def show():
    query = "select * from passwords;"
    result = sql_handler.execute(query)
    for r in result:
        website, password, username = r
        print(f"Website: {website} | Password: {password} | Username: {username}")


if __name__ == "__main__":
    cli()
