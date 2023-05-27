---
hide_table_of_contents: так
---

# Експортування поняття markdown

Цей приклад показує, як завантажувати дані з ваших сторінок понять, експортованих з прикладної дошки понять.

Спочатку експортуйте сторінки з поняттями як **Markdown &amp; CSV** за офіційними поясненнями [here](https://www.notion.so/help/export-your-content). Обов'язково виберіть `include subpages` і `Create folders for subpages.`

Потім розпакуйте завантажений файл і перемістіть розпаковану папку у своє сховище. Він повинен містити файли розмітки ваших сторінок.

Після того, як папка знаходиться у вашому сховищі, просто запустіть приклад нижче:

імпорт CodeBlock з «@theme/CodeBlock»; імпорт прикладу з «@examples/document_loaders/notion_markdown.ts»;

<CodeBlock language="typescript">{Приклад}</CodeBlock>
