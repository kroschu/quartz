імпорт CodeBlock з «@theme/CodeBlock»; імпорт OpenAIModerationExample з «@examples/chains/openai_moderation.ts»;

#  `OpenAIModerationChain`

Ви можете використовувати `OpenAIModerationChain` яка піклується про оцінку входу та виявлення того, чи порушує вона Умови надання послуг (TOS) OpenAI. Якщо на вході є будь-який вміст, що порушує умови TOS і throwError, встановлено значення true, то буде викинута і перехоплена помилка. Якщо throwError встановлено у значення false, ланцюжок поверне «Знайдено текст, який порушує політику вмісту OpenAI».

<CodeBlock language="typescript">{OpenAIModerationExample}</CodeBlock>
