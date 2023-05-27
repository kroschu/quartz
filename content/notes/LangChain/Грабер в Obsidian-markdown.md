Для створення такого скрипту я використаю Python, бібліотеки `requests`, `beautifulsoup4` і `markdownify`. Для початку, вам потрібно встановити зазначені бібліотеки, якщо у вас їх ще немає, використовуючи `pip`:

```bash
pip install requests beautifulsoup4 markdownify
```

Тепер, ми можемо створити скрипт:

```python
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
    markdown = re.sub(r'\]\((/[^)]+)\)', r'](obsidian://open?vault=YourVaultName&file=\1)', markdown)

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
```

Цей скрипт починає з вказаної URL-адреси (у нашому випадку `https://js.langchain.com/docs/`) та завантажує весь вміст відповідно до вказаної папки (у нашому випадку `langchain_docs`). Зверніть увагу, що вам потрібно замінити `YourVaultName` на назву вашого сховища Obsidian у регулярному виразі.

Виконайте цей скрипт, і він експортує сторінки у форматі Markdown та змінить внутрішні посилання на формат Obsidian.

Можливо, селектор, який використовується для знаходження вмісту на сторінці, неправильний або не відповідає структурі веб-сторінки. Щоб виправити цю проблему, спочатку перевірте структуру HTML веб-сторінки, що вас цікавить. Відкрийте сторінку в браузері, натисніть правою кнопкою миші та виберіть "Джерело сторінки" або "Переглянути код сторінки" (залежно від вашого браузера).

Знайдіть правильний селектор, який містить вміст сторінки. Тоді замініть наступний рядок у функції `download_page`:

```python
content = soup.find("div", {"class": "content"})  # Змініть селектор, якщо потрібно
```

Замініть `"div"` та `"content"` на відповідний тег та клас (або ідентифікатор), які ви знайшли. Наприклад, якщо вміст сторінки знаходиться в тегу `<article>` з класом `"main-content"`, рядок має виглядати так:

```python
content = soup.find("article", {"class": "main-content"})
```

Це повинно допомогти сценарію правильно знайти вміст на сторінках ресурсу.