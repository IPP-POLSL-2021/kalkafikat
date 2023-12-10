import typer

app = typer.Typer(help="To jest program antyplagiatowy kalkafikat")


@app.command()
def search(phrase: str = typer.Option(
    ...,
    prompt="Podaj frazę do wyszukania.",
    help="Fraza którą będzie szukać program",
    ),
):
    """
    Importuje googlesearch, tworzy generator 10 wyników wyszukiwania. Iteruje po nim tworząc listę. By zweryfikować drukuje pierwszy element listy
    """
    from googlesearch import search
    searchGenerator = search(phrase)
    links = [next(searchGenerator) for i in range(10)]
    print(links[0])

if __name__ == "__main__":
    app()
