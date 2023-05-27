імпорт CodeBlock з «@theme/CodeBlock»;

# Хрома

Chroma є відкритим вихідним кодом Apache 2.0 вбудованої бази даних.

## Налаштування

1. Запустіть chroma за допомогою Docker на вашому комп'ютері [docs](https://docs.trychroma.com/api-reference)
2. Встановіть пакет SDK Chroma JS.


```bash npm2yarn
npm install -S chromadb
```

## Документи про використання, індекс і запити

імпорт FromDocs з «@examples/indexes/vector_stores/chroma/fromDocs.ts»;

<CodeBlock language="typescript">{З документів}</CodeBlock>

## Використання, індекс і тексти запитів

імпорт FromTexts із сайту «@examples/indexes/vector_stores/chroma/fromTexts.ts»;

<CodeBlock language="typescript">{ЗТекстів}</CodeBlock>

## Використання, документація запитів з наявної колекції

імпорт пошуку з «@examples/indexes/vector_stores/chroma/search.ts»;

<CodeBlock language="typescript">{Пошук}</CodeBlock>
