{
    "id": 6,
    "query": "Identify the ID of 'Pulp Fiction' and search for torrents related to it.",
    "answers": '[{"name": "get_id", "arguments": {"q": "Pulp Fiction"}}, {"name": "search_torrents", "arguments": {"keywords": "Pulp Fiction", "quantity": 10}}]',
    "tools": [
        {
            "name": "get_id",
            "description": "Fetches the ID of a movie based on the given search query from the RapidAPI similar movies service.",
            "parameters": {
                "q": {
                    "description": "The search string for the movie title.",
                    "type": "str",
                    "default": "titanic",
                }
            },
        },
        {
            "name": "search_torrents",
            "description": "Search for torrents based on given keywords using the RapidAPI service.",
            "parameters": {
                "keywords": {
                    "description": "Keywords to search for torrents.",
                    "type": "str",
                    "default": "Meg 2 The Trench",
                },
                "quantity": {
                    "description": "Number of torrent results to return. Maximum value is 40.",
                    "type": "int",
                    "default": "40",
                },
                "page": {
                    "description": "Page number for paginated results. Defaults to 1.",
                    "type": "int, optional",
                    "default": "1",
                },
            },
        },
        {
            "name": "basic_info",
            "description": "Fetches detailed information about a cast member such as name, profession, birth and death year, bio, poster, and best titles.",
            "parameters": {
                "peopleid": {
                    "description": "The ID of the cast member whose details are to be fetched.",
                    "type": "str",
                    "default": "nm0000375",
                }
            },
        },
    ],
}
