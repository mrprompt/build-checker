import os
from click.testing import CliRunner
from checker.rpi import rpi


@pytest.mark.skip(reason="only works on real raspberry")
def test_rpi():
    runner = CliRunner()

    repository = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GITHUB_TOKEN')

    result = runner.invoke(rpi, [repository, token])

    assert result.exit_code == 0
    assert result.output == "passed\n"
