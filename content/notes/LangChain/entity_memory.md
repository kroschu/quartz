---
hide_table_of_contents: true sidebar_label: Пам'ять сутності
---

імпорт CodeBlock з «@theme/CodeBlock»;

# Пам’ять сутності

Сутність пам'яті пам'ятає дані факти про конкретні сутності в розмові. Вона витягує інформацію про суб'єкти (використовуючи LLM) і будує свої знання про цю сутність протягом довгого часу (також використовуючи LLM).

## Використання:

імпорт прикладу з «@examples/memory/entity.ts»;

<CodeBlock language="typescript">{Приклад}</CodeBlock>

### Перевірка сховища пам'яті

Ви також можете перевірити сховище пам'яті безпосередньо, щоб побачити поточне резюме кожної сутності:

імпорт MemoryInspectionExample з «@examples/memory/entity_memory_inspection.ts»;

<CodeBlock language="typescript">{MemoryInspectionExample}</CodeBlock>
