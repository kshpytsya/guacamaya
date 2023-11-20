import nox


@nox.session
def tests(session):
    session.install("pytest >= 7.4.3, == 7.*")
    session.install("pytest-check >= 2.2.2, == 2.*")
    session.install("pytest-sugar >= 0.9.7")
    # session.install("pytest-subtests >= 0.11.0, == 0.*")

    session.run("pytest")
