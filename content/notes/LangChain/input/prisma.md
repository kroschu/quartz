# Призма

Для доповнення існуючих моделей в базі даних PostgreSQL з векторним пошуком, Langchain підтримує використання [Prisma](https://www.prisma.io/) разом з PostgreSQL і [ `pgvector`](https://github.com/pgvector/pgvector) Розширення Postgres.

## Налаштування

### Інсталяція екземпляра бази даних із використанням бази даних Supabase

Зверніться до [Посібник з інтеграції з Prisma та Supabase](https://supabase.com/docs/guides/integrations/prisma) щоб налаштувати новий екземпляр бази даних за допомогою Supabase і Prisma.

### Встановити Prisma


```bash npm2yarn
npm install prisma
```

### Налаштування `pgvector` самостійне розміщення екземпляра з `docker-compose`

 `pgvector` надає попередньо створений образ Docker, який можна використовувати для швидкого налаштування власного екземпляра Postgres.


```yaml
services:
  db:
    image: ankane/pgvector
    ports:
      - 5432:5432
    volumes:
      - db:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=
      - POSTGRES_USER=
      - POSTGRES_DB=

volumes:
  db:
```

### Створити нову схему

Якщо ви ще не створили схему, створіть нову модель за допомогою `vector` поле типу `Unsupported("vector")` :


```prisma
model Document {
  id      String                 @id @default(cuid())
  content String
  vector  Unsupported("vector")?
}
```

Після цього створіть нову міграцію за допомогою `--create-only` щоб не запускати міграцію безпосередньо.


```bash npm2yarn
npx prisma migrate dev --create-only
```

Додайте наступний рядок до новоствореного перенесення, щоб увімкнути `pgvector` розширення, якщо воно ще не було увімкнене:


```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Запустіть міграцію після цього:


```bash npm2yarn
npx prisma migrate dev
```

## Використання

імпорт CodeBlock з «@theme/CodeBlock»; імпорт прикладу з «@examples/indexes/vector_stores/prisma_vectorstore/prisma.ts»; імпорт схеми з «@examples/indexes/vector_stores/prisma_vectorstore/prisma/schema.prisma»;

Використовувати `withModel` метод, щоб отримати правильний тип підказки для `metadata` поле:

<CodeBlock language="typescript">{Приклад}</CodeBlock>

У наведеному вище прикладі використовується така схема:

<CodeBlock language="prisma">{Схема}</CodeBlock>
