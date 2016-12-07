import click
import travis

@click.command('checker')
@click.argument('project', envvar='GITHUB_REPOSITORY')
@click.argument('token', envvar='GITHUB_TOKEN')
def cli(project, token):
    try:
        repo = travis.cli(project, token)

        print("Build state:" + str(repo))
    except Exception as e:
        print("An error or exception has ocurred: " + str(e))
