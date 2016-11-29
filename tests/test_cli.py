from os import environ
from click.testing import CliRunner
from checker.cli import cli


def test_cli_count():
    runner = CliRunner()
    result = runner.invoke(cli, [environ['GITHUB_REPOSITORY'], environ['GITHUB_TOKEN']])

    assert result.exit_code == 0
    assert result.output == "passed\n"
