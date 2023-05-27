---
sidebar_class_name: тільки вузол
---

імпорт CodeBlock з «@theme/CodeBlock»;

# Мій масштаб

:::tip Сумісність доступна тільки на Node.js.
:::

[MyScale](https://myscale.com/) є новою базою даних AI, яка гармонізує силу векторного пошуку та аналітики SQL, забезпечуючи керований, ефективний та чуйний досвід.

## Налаштування

1. Запуск кластера через [Веб-консоль MyScale](https://console.myscale.com/). Див. [Офіційна документація MyScale](https://docs.myscale.com/en/quickstart/) для отримання додаткової інформації.
2. Після запуску кластера, переглянути свій `Connection Details` з вашого кластера `Actions` меню. Вам знадобиться хост, порт, ім'я користувача та пароль.
3. Встановіть необхідну однорангову залежність Node.js у вашій робочій області.


```bash npm2yarn
npm install -S @clickhouse/client
```

## Документація індексів і запитів

імпорт InsertExample з «@examples/indexes/vector_stores/myscale_fromTexts.ts»;

<CodeBlock language="typescript">{InsertExample}</CodeBlock>

## Документація запиту з наявної колекції

імпорт SearchExample з «@examples/indexes/vector_stores/myscale_search.ts»;

<CodeBlock language="typescript">{SearchExample}</CodeBlock>
