
import CodeBlock from "@theme/CodeBlock";


Weaviate is an open source vector database that stores both objects and vectors, allowing for combining vector search with structured filtering. LangChain connects to Weaviate via the `weaviate-ts-client` package, the official Typescript client for Weaviate.

LangChain inserts vectors directly to Weaviate, and queries Weaviate for the nearest neighbors of a given vector, so that you can use all the LangChain Embeddings integrations with Weaviate.

## Setup

```bash npm2yarn
npm install weaviate-ts-client graphql
```

You'll need to run Weaviate either locally or on a server, see [the Weaviate documentation](https://weaviate.io/developers/weaviate/installation) for more information.

## Usage, insert documents

import InsertExample from "@examples/indexes/vector_stores/weaviate_fromTexts.ts";

<CodeBlock language="typescript">{InsertExample}</CodeBlock>

## Usage, query documents

import QueryExample from "@examples/indexes/vector_stores/weaviate_search.ts";

<CodeBlock language="typescript">{QueryExample}</CodeBlock>
