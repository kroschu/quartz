
імпорт CodeBlock з «@theme/CodeBlock»;

:::tip Сумісність доступна тільки на Node.js.
:::

HNSWLib є вектором у пам'яті, який можна зберегти у файл. Він використовує [HNSWLib](https://github.com/nmslib/hnswlib).

## Налаштування

:::увага

**У Windows**, можливо, знадобиться інсталювати [Visual Studio](https://visualstudio.microsoft.com/downloads/) спочатку для того, щоб правильно побудувати `hnswlib-node` пакунок.

:::

Ви можете встановити його за допомогою


```bash npm2yarn
npm install hnswlib-node
```

## Використання

### Створення нового покажчика з текстів

імпорт текстів ExampleTexts із сайту «@examples/indexes/vector_stores/hnswlib.ts»;

<CodeBlock language="typescript">{ПрикладТексту}</CodeBlock>

### Створити новий індекс із завантажувача

імпорт ExampleLoader з «@examples/indexes/vector_stores/hnswlib_fromdocs.ts»;

<CodeBlock language="typescript">{Завантажувач прикладів}</CodeBlock>

### Збереження покажчика до файлу та повторне завантаження

імпорт властивості ExampleSave із файлу «@examples/indexes/vector_stores/hnswlib_saveload.ts»;

<CodeBlock language="typescript">{ПрикладЗбереження}</CodeBlock>

### Фільтрувати документи

імпорт фільтра ExampleFilter із шаблону «@examples/indexes/vector_stores/hnswlib_filter.ts»;

<CodeBlock language="typescript">{ExampleFilter}</CodeBlock>
