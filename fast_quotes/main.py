"""Random Quote API"""

import random
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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

secondQuote: Quote = {
    "what": "One of the first things I cover when working with automation engineers building their first tests, either full stop or for a new project or application, is how to make their tests part of a CI build.",
    "when": "2024",
    "where": "LinkedIn",
    "who": "Bas Dijkstra"
}

thirdQuote: Quote = {
    "what": "When I first learned about eXtreme Programming 24 years ago, the publications about it were all about testing, quality, and people. And they didn't mention testers. I felt XP teams needed testing knowledge and skills, and that I, as a tester, would contribute value. I, and many others, have done so. Quite happily for everyone, including our customers!",
    "when": "2024",
    "where": "LinkedIn",
    "who": "Lisa Crispin"
}

quotes = []
quotes.append(firstQuote)
quotes.append(secondQuote)
quotes.append(thirdQuote)

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.get("/quotes")
def get_quotes():
    """Get an array of all quotes"""
    return quotes

@app.post("/quote")
async def create_quote(quote: Quote):
    """"Add a new quote"""
    quotes.append(quote)
    print(quote)
    return quote
