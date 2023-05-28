import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)"'
    matches = re.search(pattern, s)
    if matches:
        new_link = matches.group(1).replace('http:', 'https:').replace('www.', '').replace('youtube.com/embed/', 'youtu.be/')
        return new_link
    else:
        return None


if __name__ == "__main__":
    main()