---
hide_table_of_contents: так
---

#  `LatexTextSplitter`

Якщо ви хочете завантажити документи у форматі Latex, спробуйте `LatexTextSplitter`. Цей клас розділить ваш вміст на документи на основі синтаксису Latex. Наприклад, для цього параметра Latex вводить такі дані:


```latex
\begin{document}
\title{🦜️🔗 LangChain}
⚡ Building applications with LLMs through composability ⚡

\section{Quick Install}

\begin{verbatim}
Hopefully this code block isn't split
yarn add langchain
\end{verbatim}

As an open source project in a rapidly developing field, we are extremely open to contributions.

\end{document}
```

Значення `LatexTextSplitter` розділить вміст на наступні документи:

імпорт CodeBlock з «@theme/CodeBlock»; імпорт прикладу з «@examples/indexes/latex_text_splitter.ts»;

<CodeBlock language="typescript">{Приклад}</CodeBlock>
