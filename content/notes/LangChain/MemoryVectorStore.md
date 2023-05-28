
імпорт CodeBlock з «@theme/CodeBlock»;


MemoryVectorStore — це вбудоване в пам'ять векторне сховище, яке зберігає вбудовування в пам'ять і виконує точний, лінійний пошук найбільш схожих вбудованих об'єктів. Метрика подібності за замовчуванням є косинусом подібності, але її можна змінити на будь-який з метрик подібності, підтримуваних [ml-відстань](https://mljs.github.io/distance/modules/similarity.html).

## Використання

### Створення нового покажчика з текстів

імпорт текстів ExampleTexts із сайту «@examples/indexes/vector_stores/memory.ts»;

<CodeBlock language="typescript">{ПрикладТексту}</CodeBlock>

### Створити новий індекс із завантажувача

імпорт ExampleLoader з «@examples/indexes/vector_stores/memory_fromdocs.ts»;

<CodeBlock language="typescript">{Завантажувач прикладів}</CodeBlock>

### Використовувати настроюваний показник подібності

імпорт ExampleCustom з «@examples/indexes/vector_stores/memory_custom_similarity.ts»;

<CodeBlock language="typescript">{ExampleCustom}</CodeBlock>
