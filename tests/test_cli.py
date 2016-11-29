import os
from click.testing import CliRunner
from checker.cli import cli


def test_cli_count():
    runner = CliRunner()

    repository = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GITHUB_TOKEN')

    result = runner.invoke(cli, [repository, token])

    assert result.exit_code == 0
    assert result.output == "passed\n"
