---
hide_table_of_contents: true sidebar_label: зведення розмови
---

імпорт CodeBlock з «@theme/CodeBlock»;

# Зведена пам’ять розмови

У зведеній пам'яті розмови підсумовується розмова в міру її виникнення та зберігає поточне зведення в пам'яті. Ця пам'ять потім може бути використана для введення резюме розмови до цих пір в підказку / ланцюжок. Ця пам'ять є найбільш корисною для тривалих розмов, де збереження історії минулих повідомлень в запиті дослівно займе занадто багато знаків.

## Використання, з LLM

імпорт TextExample з «@examples/memory/summary_llm.ts»;

<CodeBlock language="typescript">{Приклад тексту}</CodeBlock>

## Використання, з моделлю чату

імпорт ChatExample з «@examples/memory/summary_chat.ts»;

<CodeBlock language="typescript">{ChatExample}</CodeBlock>
