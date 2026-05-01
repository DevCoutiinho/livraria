import click
from flask.cli import with_appcontext
from app.seeds.manager_seed import run_all_seeds

@click.command('seed')
@with_appcontext
def seed_command():
    """Executar seeders"""
    run_all_seeds()
    click.echo('Seeders executadas com sucesso!')