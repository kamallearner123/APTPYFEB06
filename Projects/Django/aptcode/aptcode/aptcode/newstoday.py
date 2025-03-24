import feedparser
import re
import os

def get_todays_news():
    CWD = os.path.dirname(os.path.realpath(__file__))
    NEWS_HTML_FILE = CWD+"/data/newstoday.html"

    # URL of The Hindu's main RSS feed
    rss_url = 'https://www.thehindu.com/feeder/default.rss'

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Display the feed title
    print(f"Feed Title: {feed.feed.title}\n")

    # Keys words
    keywords = ["Block Chain","IOT","Bitcoin","India"]

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The Hindu News Feed</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f8f9fa;
            }}
            .news-container {{
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h2 {{
                color: #0056b3;
            }}
            a {{
                text-decoration: none;
                color: #007bff;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .news-item {{
                border-bottom: 1px solid #ddd;
                padding: 15px 0;
            }}
        </style>
    </head>
    <body>
        <div class="news-container">
            <h1>{feed.feed.title}</h1>
    """

    parsed_data = ""
    startExp = ".*\\s"
    endExp = ".*"

    with open(NEWS_HTML_FILE, "w") as fd:
        # Iterate through the feed entries and display details
        for entry in feed.entries:
            for keyoword in keywords:
                exp = startExp+keyoword+endExp
                if re.match(exp,entry.title,re.IGNORECASE):
                    parsed_data += f"""
                        <div class="news-item">
                            <h2><a href="{entry.link}" target="_blank">{entry.title}</a></h2>
                            <p><strong>Published:</strong> {entry.published}</p>
                            <p>{entry.summary}</p>
                        </div>
                    """
        fd.write(parsed_data)
        fd.write( """
            </div>
        </body>
        </html>
        """)