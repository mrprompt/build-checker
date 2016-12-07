import os
import checker.travis as cli


def test_travis():
    repository = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GITHUB_TOKEN')

    result = cli.cli(repository, token)

    assert result != ""


def test_withou_token():
    repository = os.environ.get('GITHUB_REPOSITORY')
    result = cli.cli(repository)

    assert result != ""


def test_without_parameters():
    result = cli.cli()

    assert result in ["[403] not a Travis user", "[403] Forbidden"]
