# cli.py
import click
from handlers import text_gen, explain_code, fix_regex, explain_shell

@click.group()
def cli():
    """gpt-helper-cli: AI-powered command-line tool."""
    pass

@cli.command()
@click.argument("prompt")
def text(prompt):
    """Generate text from a prompt."""
    result = text_gen.handle(prompt)
    click.echo(result)

@cli.command()
@click.option("-f", "--file", help="Path to code file", required=False)
@click.argument("code", required=False)
def explain_code_cmd(code, file):
    """Explain source code from a string or file."""
    if file:
        with open(file) as f:
            code = f.read()
    result = explain_code.handle(code)
    click.echo(result)

@cli.command()
@click.argument("regex")
def fix_regex_cmd(regex):
    """Fix and explain a regex."""
    result = fix_regex.handle(regex)
    click.echo(result)

@cli.command()
@click.argument("command")
def explain_shell_cmd(command):
    """Explain a shell command."""
    result = explain_shell.handle(command)
    click.echo(result)

if __name__ == "__main__":
    cli()
