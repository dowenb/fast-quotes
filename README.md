# Fast Quotes

## Run

```
uvicorn fast_quotes.main:app --reload
```

## Call the API

Note: Examples using [HTTPie](https://httpie.io/)

```
# Add Quote
http POST http://localhost:8000/quote who=ben what=random when=today where=today

# Get Random Quote
http POST http://localhost:8000/quote
```
