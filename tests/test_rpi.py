import os

from checker.rpi import cli
from click.testing import CliRunner


def test_rpi():
    runner = CliRunner()

    repository = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GITHUB_TOKEN')

    result = runner.invoke(cli, [repository, token])

    assert result.exit_code == 0
