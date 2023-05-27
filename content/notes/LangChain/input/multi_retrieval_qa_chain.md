імпорт CodeBlock з «@theme/CodeBlock»; імпорт MultiRetrievalQAExample з «@examples/chains/multi_retrieval_qa.ts»;

#  `MultiRetrievalQAChain`

MultiRetrievalQAChain дозволяє LLM вибирати з декількох ретриверів. Створіть ланцюжок, надавши колекцію векторних магазинів (як ретриверів) разом з відповідними іменами та описами. Ланцюжок отримує запит на вхід, обирає відповідних отримувачів, а потім подає його до вибраних отримувачів.

<CodeBlock language="typescript">{MultiRetrievalQAExample}</CodeBlock>
