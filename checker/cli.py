import click
from travispy import TravisPy


@click.command('checker')
@click.argument('project', envvar='GITHUB_REPOSITORY')
@click.argument('token', envvar='GITHUB_TOKEN')
def cli(project, token):
    try:
        travis = TravisPy.github_auth(token)
        repo = travis.repo(project)

        print(repo['last_build_state'])
    except Exception as e:
        print("An error or exception has ocurred: " + str(e))
