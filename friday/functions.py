import webbrowser



def open_website(url):
    webbrowser.open(url)


functions = [
    {
        "name": "open_website",
        "description": "Opens a website in the browser",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL of the website to open",
                },
            },
            "required": ["url"],
        },
    }
]