import re
import json
import requests
import pandas as pd
from datetime import datetime

ghcn_url = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/"

regex_pattern = ('(\\w+.\\w{3})</a></td><td align="right">(\\d{4}-\\d{2}-\\d{2}\\s\\d{2}\\:\\d{2})\\s*</td><td '
                 'align="right">\\s*(\\d+)(\\w*)')
compiled_regex = re.compile(regex_pattern)


def get_files(html_content, date_threshold):
    print("get files")
    matches = []
    for line in html_content.splitlines():
        file_info = compiled_regex.findall(line)
        if len(file_info) > 0:
            matches.extend(compiled_regex.findall(line))
    df = pd.DataFrame(matches, columns=['file_name', 'last_modified', 'size_value', 'size_unit'])
    df['last_modified'] = pd.to_datetime(df['last_modified'], format='%Y-%m-%d %H:%M')
    df = df[df['last_modified'] > date_threshold]
    return df


def lambda_handler(event, context):
    r = requests.get(ghcn_url)
    today = datetime.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    date_threshold = today.strftime('%Y-%m-%d')
    files_df = get_files(r.text, date_threshold)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "OK",
            # "location": ip.text.replace("\n", "")
        }),
    }
