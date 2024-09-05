import argparse
import json
from docs_parser.parser import Parser

def main() -> None:
    args = parse_arguments()
    data = read_file(args.filepath)
    parser = Parser()
    parsed_data = parser.parse(data)
    print(parsed_data)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Parse satisfactory docs.json file')
    parser.add_argument('filepath', type=str, help='The path of the docs.json file to parse')
    return parser.parse_args()

def read_file(filepath: str) -> dict:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("File is empty")
            return json.loads(content)
    except UnicodeDecodeError as e:
        raise ValueError(f"Encoding error in file: {filepath}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON content in file: {filepath}") from e

if __name__ == '__main__':
    main()