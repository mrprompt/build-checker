from travispy import TravisPy


def cli(project="", token=""):
    """ Check build on Travis CI and return this status """
    try:
        travis = TravisPy.github_auth(token)
        repo = travis.repo(project)

        return str(repo['last_build_state'])
    except Exception as e:
        return str(e)
