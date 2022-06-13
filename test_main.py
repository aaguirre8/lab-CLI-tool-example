from click.testing import CliRunner
from main import search

# search(path, ftype)


def test_search():
    runner = CliRunner()
    result = runner.invoke(search, ['--path', '.', 'ftype', 'py'])
    assert result.exit_code == 0
    assert '.py' in result.output


