from click.testing import CliRunner

from checker.cli import cli


def test_cli_count():
    runner = CliRunner()
    result = runner.invoke(cli, ['mrprompt/CaixaEconomicaFederal', '1e32aa8d0fceec3eb73e9a2f8a837ebdab6ba6db'])

    assert result.exit_code == 0
    assert result.output == "passed\n"
