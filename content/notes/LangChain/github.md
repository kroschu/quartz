---
sidebar_class_name: node-only hide_table_of_contents: true
---

# GitHub

У цьому прикладі описано, як завантажувати дані зі сховища GitHub. Ви можете встановити `GITHUB_ACCESS_TOKEN` змінна середовища на токен доступу GitHub для збільшення ліміту швидкості та доступу до приватних репозиторіїв.

## Налаштування

Завантажувач GitHub вимагає [ігнорувати пакет npm](https://www.npmjs.com/package/ignore) як рівноправна залежність. Встановити його наступним чином:


```bash npm2yarn
npm install ignore
```

## Використання

імпорт CodeBlock з «@theme/CodeBlock»; імпорт прикладу з «@examples/document_loaders/github.ts»;

<CodeBlock language="typescript">{Приклад}</CodeBlock>

Завантажувач буде ігнорувати бінарні файли, такі як зображення.

### Використання синтаксису .gitignore

Щоб ігнорувати певні файли, ви можете передати їх `ignorePaths` створити масив у конструкторі:

імпорт IgnoreExample з «@examples/document_loaders/github_ignore_paths.ts»;

<CodeBlock language="typescript">{IgnoreExample}</CodeBlock>
