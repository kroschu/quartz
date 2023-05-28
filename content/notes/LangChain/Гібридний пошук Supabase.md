

Ланчлайн підтримує гібридний пошук за допомогою бази даних Supabase Postgres. Гібридний пошук поєднує розширення Postgres pgvector (пошук за схожістю) та повнотекстовий пошук (пошук за ключовими словами) для пошуку документів. Ви можете додавати документи за допомогою функції SupabaseVectorStore addDocuments. SupabaseHybridKeyWordSearch приймає як параметри вбудовування, клієнт supabase, кількість результатів для пошуку за схожістю та кількість результатів для пошуку за ключовим словом. Функція getRelevantDocuments створює список документів, з яких видалено дублікати, відсортований за показником релевантності.

## Setup

### Install the library with

```bash npm2yarn
npm install -S @supabase/supabase-js
```

### Create a table and search functions in your database

Run this in your database:

```sql
-- Enable the pgvector extension to work with embedding vectors
create extension vector;

-- Create a table to store your documents
create table documents (
  id bigserial primary key,
  content text, -- corresponds to Document.pageContent
  metadata jsonb, -- corresponds to Document.metadata
  embedding vector(1536) -- 1536 works for OpenAI embeddings, change if needed
);

-- Create a function to similarity search for documents
create function match_documents (
  query_embedding vector(1536),
  match_count int,
  filter jsonb DEFAULT '{}'
) returns table (
  id bigint,
  content text,
  metadata jsonb,
  similarity float
)
language plpgsql
as $$
#variable_conflict use_column
begin
  return query
  select
    id,
    content,
    metadata,
    1 - (documents.embedding <=> query_embedding) as similarity
  from documents
  where metadata @> filter
  order by documents.embedding <=> query_embedding
  limit match_count;
end;
$$;

-- Create a function to keyword search for documents
create function kw_match_documents(query_text text, match_count int)
returns table (id bigint, content text, metadata jsonb, similarity real)
as $$

begin
return query execute
format('select id, content, metadata, ts_rank(to_tsvector(content), plainto_tsquery($1)) as similarity
from documents
where to_tsvector(content) @@ plainto_tsquery($1)
order by similarity desc
limit $2')
using query_text, match_count;
end;
$$ language plpgsql;
```

## Usage

import CodeBlock from "@theme/CodeBlock";
import Example from "@examples/retrievers/supabase_hybrid.ts";

<CodeBlock language="typescript">{Example}</CodeBlock>
