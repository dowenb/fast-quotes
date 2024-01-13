"""Random Quote API"""

import random
from fastapi import FastAPI
from pydantic import BaseModel

class Quote(BaseModel):
    who: str
    what: str
    when: str
    where: str

firstQuote: Quote = {
    "what": "All models are wrong, but some are useful.",
    "when": "1976",
    "where": "Published in the Journal of the American Statistical Association.",
    "who": "George Box"
}

quotes = []
quotes.append(firstQuote)

app = FastAPI()


@app.get("/health")
def read_root():
    """Health Check"""
    return {"STATUS": "OK"}

@app.get("/quote")
def get_quote():
    """Get a random quote"""
    random_quote = random.choice(quotes)
    print(random_quote)
    return random_quote

@app.post("/quote")
async def create_quote(quote: Quote):
    """"Add a new quote"""
    quotes.append(quote)
    print(quote)
    return quote
