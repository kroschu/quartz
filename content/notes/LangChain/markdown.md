---
hide_table_of_contents: так
---

#  `MarkdownTextSplitter`

Якщо ваш вміст має формат Markdown, тоді `MarkdownTextSplitter`. Цей клас поділить ваш вміст на документи на основі заголовків Markdown. Наприклад, якщо у вас є наступний вміст Markdown:


```markdown
# Header 1

This is some content.

## Header 2

This is some more content.

# Header 3

This is even more content.
```

Потім `MarkdownTextSplitter` розділить вміст на три документи:


```typescript
import { MarkdownTextSplitter } from "langchain/text_splitter";

const text = `# Header 1

This is some content.

## Header 2

This is some more content.

# Header 3

This is even more content.`;

const splitter = new MarkdownTextSplitter();

const output = await splitter.createDocuments([text], {
  metadata: "something",
});
/*
[
  {
    "pageContent": "# Header 1\n\nThis is some content.",
    "metadata": "something"
  },
  {
    "pageContent": "## Header 2\n\nThis is some more content.",
    "metadata": "something"
  },
  {
    "pageContent": "# Header 3\n\nThis is even more content.",
    "metadata": "something"
  }
]
*/
```
