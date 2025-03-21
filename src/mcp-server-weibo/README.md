# MCP Server Weibo

A Weibo crawler server for MCP (Model Control Protocol) that provides functionality to fetch user profiles, feeds, and search for users on Weibo.

## Features

- Search Weibo users by keyword
- Get user profile information
- Fetch user's Weibo feeds with pagination support

## Installation

```bash
pip install mcp-server-weibo
```

## Usage

```python
from mcp_server_weibo import WeiboCrawler

# Create a crawler instance
crawler = WeiboCrawler()

# Search for users
users = await crawler.search_weibo_users("keyword", limit=10)

# Get user profile
profile = await crawler.extract_weibo_profile("user_id")

# Get user feeds
feeds = await crawler.extract_weibo_feeds("user_id", limit=20)
```

## Requirements

- Python >= 3.8
- httpx >= 0.24.0
- pydantic >= 2.0.0
- fastmcp >= 0.1.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.
