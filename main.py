#! virtualenv path
import click
import glob

@click.command()
@click.option(
    '--path',
    prompt='Path to search csv files',
    help='This is the path to search for files: /tmp',
)
@click.option(
    '--ftype', prompt='Pass in the type of file', help='File type to look for: i.e csv'
)

def search(path, ftype):
    results = glob.glob(f"{path}/*{ftype}")
    click.echo(click.style("Found Matches:", fg='red'))
    for result in results:
        click.echo(click.style(f"{result}", bg="yellow", fg="white"))

if __name__=='__main__':
    search()

# Local script execution
# python main.py --path . --ftype py