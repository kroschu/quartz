---
sidebar_position: 3 sidebar_label: інтеграція
---

імпорт CodeBlock з «@theme/CodeBlock»;

# Інтеграції: LLM

LangChain пропонує ряд реалізацій LLM, які інтегруються з різними постачальниками моделей. Це:

##  `OpenAI`


```typescript
import { OpenAI } from "langchain/llms/openai";

const model = new OpenAI({
  temperature: 0.9,
  openAIApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.OPENAI_API_KEY
});
const res = await model.call(
  "What would be a good company name a company that makes colorful socks?"
);
console.log({ res });
```

## Лазуровий `OpenAI`


```typescript
import { OpenAI } from "langchain/llms/openai";

const model = new OpenAI({
  temperature: 0.9,
  azureOpenAIApiKey: "YOUR-API-KEY",
  azureOpenAIApiInstanceName: "YOUR-INSTANCE-NAME",
  azureOpenAIApiDeploymentName: "YOUR-DEPLOYMENT-NAME",
  azureOpenAIApiVersion: "YOUR-API-VERSION",
});
const res = await model.call(
  "What would be a good company name a company that makes colorful socks?"
);
console.log({ res });
```

## Google Вершина AI

Реалізація Vertex AI призначена для використання в Node.js, а не безпосередньо в браузері, оскільки вона вимагає обліковий запис служби, щоб використовувати.

Перш ніж запускати цей код, переконайтеся, що API Vertex AI увімкнуто для відповідного проекту на приладній дошці Google Cloud, і ви пройшли автентифікацію в Google Cloud, використовуючи один із цих методів:

- Ви увійшли в обліковий запис (за допомогою `gcloud auth application-default login`) дозволена для цього проекту.
- Ви працюєте на комп’ютері з обліковим записом служби, дозволеним для цього проекту.
- Завантажено облікові дані для облікового запису служби, дозволеного для проекту, і встановлено `GOOGLE_APPLICATION_CREDENTIALS` змінна середовища до шляху до цього файла.


```bash npm2yarn
npm install google-auth-library
```

імпорт GoogleVertexAIExample з «@examples/llms/googlevertexai.ts»;

<CodeBlock language="typescript">{GoogleVertexAIExample}</CodeBlock>

##  `HuggingFaceInference`


```bash npm2yarn
npm install @huggingface/inference@1
```


```typescript
import { HuggingFaceInference } from "langchain/llms/hf";

const model = new HuggingFaceInference({
  model: "gpt2",
  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.HUGGINGFACEHUB_API_KEY
});
const res = await model.call("1 + 1 =");
console.log({ res });
```

##  `Cohere`


```bash npm2yarn
npm install cohere-ai
```


```typescript
import { Cohere } from "langchain/llms/cohere";

const model = new Cohere({
  maxTokens: 20,
  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.COHERE_API_KEY
});
const res = await model.call(
  "What would be a good company name a company that makes colorful socks?"
);
console.log({ res });
```

##  `Replicate`


```bash npm2yarn
npm install replicate
```


```typescript
import { Replicate } from "langchain/llms/replicate";

const model = new Replicate({
  model:
    "daanelson/flan-t5:04e422a9b85baed86a4f24981d7f9953e20c5fd82f6103b74ebc431588e1cec8",
  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.REPLICATE_API_KEY
});
const res = await modelA.call(
  "What would be a good company name a company that makes colorful socks?"
);
console.log({ res });
```

## AWS `SageMakerEndpoint`

Перевірка [Швидкий запуск Amazon SageMaker](https://aws.amazon.com/sagemaker/jumpstart/) для списку доступних моделей, і як розгорнути свій власний.


```bash npm2yarn
npm install @aws-sdk/client-sagemaker-runtime
```

імпорт SageMakerEndpointExample з «@examples/models/llm/sagemaker_endpoint.ts»;

<CodeBlock language="typescript">{SageMakerEndpointExample}</CodeBlock>

## Додаткові реалізації LLM

###  `PromptLayerOpenAI`

LangChain інтегрується з PromptLayer для реєстрації та відлагодження запитів та відповідей. Щоб додати підтримку PromptLayer:

1. Створіть обліковий запис PromptLayer тут: [https://promptlayer.com](https://promptlayer.com).
2. Створіть токен API та передайте його як `promptLayerApiKey` аргумент у `PromptLayerOpenAI` конструктор або в `PROMPTLAYER_API_KEY` змінна середовища.


```typescript
import { PromptLayerOpenAI } from "langchain/llms/openai";

const model = new PromptLayerOpenAI({
  temperature: 0.9,
  openAIApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.OPENAI_API_KEY
  promptLayerApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.PROMPTLAYER_API_KEY
});
const res = await model.call(
  "What would be a good company name a company that makes colorful socks?"
);
```

### Лазуровий `PromptLayerOpenAI`

LangChain інтегрується з PromptLayer для реєстрації та відлагодження запитів та відповідей. Щоб додати підтримку PromptLayer:

1. Створіть обліковий запис PromptLayer тут: [https://promptlayer.com](https://promptlayer.com).
2. Створіть токен API та передайте його як `promptLayerApiKey` аргумент у `PromptLayerOpenAI` конструктор або в `PROMPTLAYER_API_KEY` змінна середовища.


```typescript
import { PromptLayerOpenAI } from "langchain/llms/openai";

const model = new PromptLayerOpenAI({
  temperature: 0.9,
  azureOpenAIApiKey: "YOUR-AOAI-API-KEY", // In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
  azureOpenAIApiInstanceName: "YOUR-AOAI-INSTANCE-NAME", // In Node.js defaults to process.env.AZURE_OPENAI_API_INSTANCE_NAME
  azureOpenAIApiDeploymentName: "YOUR-AOAI-DEPLOYMENT-NAME", // In Node.js defaults to process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME
  azureOpenAIApiCompletionsDeploymentName:
    "YOUR-AOAI-COMPLETIONS-DEPLOYMENT-NAME", // In Node.js defaults to process.env.AZURE_OPENAI_API_COMPLETIONS_DEPLOYMENT_NAME
  azureOpenAIApiEmbeddingsDeploymentName:
    "YOUR-AOAI-EMBEDDINGS-DEPLOYMENT-NAME", // In Node.js defaults to process.env.AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME
  azureOpenAIApiVersion: "YOUR-AOAI-API-VERSION", // In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
  promptLayerApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.PROMPTLAYER_API_KEY
});
const res = await model.call(
  "What would be a good company name a company that makes colorful socks?"
);
```

Запит і відповідь будуть зареєстровані в [Приладна дошка PromptLayer](https://promptlayer.com/home).

> **_Примітка:_** У режимі потокової передачі PromptLayer не запише відповідь.
