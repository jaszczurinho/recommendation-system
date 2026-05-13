from pydantic import BaseModel, Field
from typing import List

class Filters(BaseModel):
    genres: List[str] = Field(
        description="A list of specific literary genres explicitly requested by the user. Acts as a strict inclusion filter (e.g., 'Mystery', 'Sci-Fi')."
    )
    authors: List[str] = Field(
        description="A list of specific authors the user explicitly wants to read. Only include if the user names them directly as a requirement."
    )

class Preferences(BaseModel):
    themes: List[str] = Field(
        description="Key themes, topics, or subject matters the user enjoys (e.g., 'time travel', 'friendship'). Used for ranking results."
    )
    tone: List[str] = Field(
        description="The desired mood, atmosphere, or emotional tone of the book (e.g., 'dark', 'uplifting', 'humorous', 'tense')."
    )

class References(BaseModel):
    books: List[str] = Field(
        description="Titles of books mentioned by the user as positive examples or context for what they like. Do not include books they disliked."
    )
    authors: List[str] = Field(
        description="Authors mentioned by the user as positive examples of their preference. Do not include authors they disliked."
    )

class Exclusions(BaseModel):
    genres: List[str] = Field(
        description="Genres that the user explicitly dislikes or wants to avoid."
    )
    authors: List[str] = Field(
        description="Specific authors the user does not want to read."
    )
    tone: List[str] = Field(
        description="Specific moods, atmospheres, or emotional tones the user explicitly wants to avoid (e.g.,'depressing')." 
    )

class UserRequest(BaseModel):
    filters: Filters
    preferences: Preferences
    references: References
    exclusions: Exclusions
