from travispy import TravisPy

def cli(project, token):
    try:
        travis = TravisPy.github_auth(token)
        repo = travis.repo(project)

        return str(repo['last_build_state'])
    except Exception as e:
        return str(e)
