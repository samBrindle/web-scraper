import requests
from bs4 import BeautifulSoup

def get_info(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    return soup.find_all('p')

def get_citations_needed_report(url):
    string = ""

    paragraphs = get_info(url)

    for para in paragraphs:
        if "citation needed" in para.text:
            string += para.text + "\n"

    print(string)

def get_citations_needed_count(url):
    count = 0
    paragraphs = get_info(url)

    for para in paragraphs:
        if "citation needed" in para.text:
            count += 1

    print(count)
    return count

get_citations_needed_count("https://en.wikipedia.org/wiki/Discord")
get_citations_needed_report("https://en.wikipedia.org/wiki/Discord")
