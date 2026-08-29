import re
import pandas as pd
import os

LOG_PARSER = re.compile(
    r'\[(?P<timestamp>[^\]]+)\] '          
    r'\[(?P<severity>[^\]]+)\] '            
    r'(?:\[client (?P<ip>[^\]]+)\] )?'      
    r'(?P<message>.*)'
)
def parse_log_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR: Cant find '{file_path}'.")
        return pd.DataFrame()
    parsed_data = []

    with open(file_path, 'r') as f:
        for line in f:
            match = LOG_PARSER.match(line)
            if match:
                parsed_data.append(match.groupdict())

    df = pd.DataFrame(parsed_data)
    df =  df.dropna(subset=['ip'])
    return df

if __name__ == "__main__":
    log_file_path = "data/Apache_2k.log"
    print(f"parsing {log_file_path}...")
    traffic_df = parse_log_file(log_file_path)

    print("\nExtraction complete... here are 5 rows:")
    print(traffic_df.head())
    print(f"\nTotal extracted web requests: {len(traffic_df)}")
    