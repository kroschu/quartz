import os
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def download_page(url, output_folder):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", {"class": "content"})  # Змініть селектор, якщо потрібно

    if not content:
        print(f"Не вдалося знайти вміст на сторінці: {url}")
        return

    title = soup.find("title").text
    filename = f"{title}.md"
    output_path = os.path.join(output_folder, filename)

    markdown = md(str(content))
    markdown = re.sub(r'\]\((/[^)]+)\)', r'](obsidian://open?vault=content&file=\1)', markdown)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(markdown)

    print(f"Завантажено: {url} -> {output_path}")

def grab_website(start_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    to_visit = [start_url]
    visited = set()

    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue

        visited.add(url)

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            href = link["href"]

            if href.startswith("/"):
                full_url = f"https://js.langchain.com{href}"
                if full_url not in visited:
                    to_visit.append(full_url)

        download_page(url, output_folder)

if __name__ == "__main__":
    start_url = "https://js.langchain.com/docs/"
    output_folder = "langchain_docs"

    grab_website(start_url, output_folder)