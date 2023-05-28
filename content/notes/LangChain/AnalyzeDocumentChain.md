імпорт CodeBlock з «@theme/CodeBlock»; імпорт AnalyzeDocumentExample з «@examples/chains/analyze_document_chain_summarize.ts»;


Ви можете використовувати `AnalyzeDocumentChain`, яка приймає один шматок тексту як вхід і працює над ним. Цей ланцюжок піклується про поділ тексту, а потім передачу його на `MapReduceDocumentsChain` для створення резюме.

<CodeBlock language="typescript">{AnalyzeDocumentExample}</CodeBlock>
