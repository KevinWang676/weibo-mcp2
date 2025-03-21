from typing import Union
from pydantic import BaseModel

class PagedFeeds(BaseModel):
    """
    Data model for paginated Weibo feeds.
    
    Attributes:
        SinceId (Union[int, str]): ID of the last feed for pagination
        Feeds (list[dict]): List of Weibo feed entries
    """
    SinceId: Union[int, str]
    Feeds: list[dict]

class SearchResult(BaseModel):
    """
    Data model for Weibo user search results.
    
    Attributes:
        Id (Union[int, str]): User's unique identifier
        NickName (str): User's display name
        AvatarHD (str): URL to user's high-resolution avatar image
        Description (str): User's profile description
    """
    Id: str
    NickName: str
    AvatarHD: str
    Description: str