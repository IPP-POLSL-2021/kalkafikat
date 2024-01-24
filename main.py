import typer
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
import kfmodes


app = typer.Typer(help="To jest program antyplagiatowy kalkafikat")


@app.command()
def check(path: str = typer.Option(
    ...,
    prompt="Podaj ścieżkę pliku do analizy",
    help="Tryb nr 1. Wklej ścieżkę do jednego pliku.",
    ),
):
    """
    Porównuje dany kod z bazą kodu. Zwraca procent plagiatu. Dodaje porównywany kod w formie ztokenizowanej do bazy.
    """
    try:
        print(f"Procent plagiatu {path.split('/')[-1]}: {kfmodes.check(path)}")
    except FileNotFoundError:
        pass

@app.command()
def compare(path1: str = typer.Option(
    ...,
    prompt="Podaj ścieżkę do pierwszego pliku.",
    help="Tryb nr 2. Ścieżka do pierwszego pliku.",
    ), path2: str = typer.Option(...,
    prompt="Podaj ścieżkę do drugiego pliku.",
    help="Tryb nr 2. Ścieżka do drugiego pliku." 
)):
    """
    Porównuje dwa pliki z kodem. Zwraca procent plagiatu.
    """
    try:
        print(f"Procent plagiatu {path1.split('/')[-1]} względem {path2.split('/')[-1]}: {kfmodes.compare(path1, path2)}")
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    app()