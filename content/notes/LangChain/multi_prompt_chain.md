імпорт CodeBlock з «@theme/CodeBlock»; імпорт MultiPromptExample з «@examples/chains/multi_prompt.ts»;

#  `MultiPromptChain`

MultiPromptChain дозволяє LLM вибрати з декількох запитів. Створіть ланцюжок, надавши колекцію шаблонів/запитів разом із відповідними іменами та описами. Ланцюжок бере на вхід рядок, обирає відповідний запит і згодом подає його до обраного запиту.

<CodeBlock language="typescript">{MultiPromptExample}</CodeBlock>
