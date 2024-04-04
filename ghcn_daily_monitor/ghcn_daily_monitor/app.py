import re
import json

import requests
ghcn_url = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/"

regex_pattern = ('(\\w+.\\w{3})</a></td><td align="right">(\\d{4}-\\d{2}-\\d{2}\\s\\d{2}\\:\\d{2})\\s*</td><td '
                 'align="right">\\s*(\\d+)(\\w*)')
compiled_regex = re.compile(regex_pattern)


def get_files(html_content):
    print("get files")
    matches = []
    for line in html_content.splitlines():
        file_info = compiled_regex.findall(line)
        if len(file_info) > 0:
            matches.extend(compiled_regex.findall(line))
    return matches


def lambda_handler(event, context):
    r = requests.get(ghcn_url)
    get_files(r.text)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "OK",
            # "location": ip.text.replace("\n", "")
        }),
    }
