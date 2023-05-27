---
hide_table_of_contents: істинна бічна панель_позиція: 3
---

імпорт CodeBlock з «@theme/CodeBlock»; імпорт ConvoRetrievalQAExample з «@examples/chains/conversational_qa.ts»;

# Розмовний пошук QA

Значення `ConversationalRetrievalQA` ланцюг будується `RetrievalQAChain` надати компонент історії чату.

Це вимагає двох входів: питання і історію чату. Спочатку він об'єднує історію чату та питання в окреме питання, а потім шукає відповідні документи від ретривера, а потім передає ці документи та питання до ланцюжка відповідей на запитання, щоб повернути відповідь.

Для його створення знадобиться ретривер. У наведеному нижче прикладі ми створимо один з vectorstore, який можна створити з вкладених файлів.

імпорт прикладу з «@examples/chains/conversational_qa.ts»;

<CodeBlock language="typescript">{ConvoRetrievalQAExample}</CodeBlock>

У цьому фрагменті коду, методом fromLLM `ConversationalRetrievalQAChain` клас має наступний підпис:


```typescript
static fromLLM(
  llm: BaseLanguageModel,
  retriever: BaseRetriever,
  options?: {
    questionGeneratorTemplate?: string;
    qaTemplate?: string;
    returnSourceDocuments?: boolean;
  }
): ConversationalRetrievalQAChain
```

Ось пояснення кожного з атрибутів об’єкта параметрів:

-  `questionGeneratorTemplate` : Рядок, який визначає шаблон створення питання. Якщо передбачено, `ConversationalRetrievalQAChain` цей шаблон буде використано для створення питання з контексту розмови, а не для використання параметра питання. Це може бути корисним, якщо початкове питання не містить достатньо інформації для отримання правильної відповіді.
-  `qaTemplate` : Рядок, який визначає шаблон відповіді. Якщо передбачено, `ConversationalRetrievalQAChain` цей шаблон використовуватиметься для форматування відповіді перед поверненням результату. Це може бути корисним, якщо ви хочете налаштувати спосіб представлення відповіді кінцевому користувачу.
-  `returnSourceDocuments` : логічне значення, яке вказує, чи `ConversationalRetrievalQAChain` слід повернути вихідні документи, які використовувалися для отримання відповіді. Якщо встановити значення true, документи буде включено до результату, який повертає метод call(). Це може бути корисно, якщо ви хочете, щоб користувач міг бачити джерела, що використовуються для створення відповіді. Якщо його не встановлено, типовим значенням буде false.

Підсумовуючи, `questionGeneratorTemplate`, `qaTemplate`, і `returnSourceDocuments` параметри дозволяють користувачеві налаштувати поведінку `ConversationalRetrievalQAChain`
