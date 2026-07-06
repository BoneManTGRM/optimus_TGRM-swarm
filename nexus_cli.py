import typer
from rich.console import Console
app = typer.Typer()
@app.command()
def run(cycles: int = 20, visualize: bool = True):
    print('🚀 Full Nexus Swarm CLI activated - Advanced mode engaged')
    # Full simulation here
if __name__ == "__main__":
    app()