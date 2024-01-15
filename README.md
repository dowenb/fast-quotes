# Fast Quotes

## Install dependencies

This project uses [poetry](https://python-poetry.org/) for managing dependencies.

```
poetry install
```

## Run

```
uvicorn fast_quotes.main:app --reload
```

## Call the API

Note: Examples using [HTTPie](https://httpie.io/)

```
# Add Quote
http POST http://localhost:8000/quote who=ben what=random when=today where=BBC

# Get Random Quote
http http://localhost:8000/quote
```
