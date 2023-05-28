
імпорт CodeBlock з «@theme/CodeBlock»; імпорт прикладу з «@examples/models/llm/llm_streaming_stdout.ts»;



Цей підручник дає вам короткий огляд про створення наскрізної мовної моделі програми з LangChain.

## Інсталяція та настроювання

Щоб почати роботу, виконайте наведені нижче дії. [інструкції з інсталяції](./install) щоб встановити LangChain.

## Отримання LLM

Використання LangChain, як правило, вимагає інтеграції з одним або декількома постачальниками моделей, сховищ даних, api і т.д.

У цьому прикладі ми будемо використовувати API OpenAI, тому ніяких додаткових налаштувань не потрібно.

## Створення програми мовної моделі

Тепер, коли ми встановили LangChain, ми можемо почати будувати нашу програму мовної моделі.

LangChain надає багато модулів, які можуть бути використані для створення додатків мовних моделей. Модулі можуть бути об'єднані для створення більш складних додатків, або використовуватися окремо для простих додатків.

### LLM: отримати прогнози від мовної моделі

Найбільш основним блоком збірки LangChain є виклик LLM на деяких вхідних даних. Давайте розглянемо простий приклад того, як це зробити. Для цього давайте зробимо вигляд, що ми будуємо сервіс, який формує назву компанії на основі того, що робить компанія.

Для того, щоб зробити це, спочатку потрібно імпортувати обгортку LLM.


```typescript
import { OpenAI } from "langchain/llms/openai";
```

Тоді нам потрібно буде встановити змінну середовища для ключа OpenAI. Три варіанти тут:

1. Ми можемо зробити це, встановивши значення в `.env` файл і використовувати [dotenv](https://github.com/motdotla/dotenv) пакунок для читання.

   1.1. Для Api OpenAI


   ```bash
   OPENAI_API_KEY="..."
   ```

   1.2. Для Azure OpenAI:


   ```bash
   AZURE_OPENAI_API_KEY="..."
   AZURE_OPENAI_API_INSTANCE_NAME="..."
   AZURE_OPENAI_API_DEPLOYMENT_NAME="..."
   AZURE_OPENAI_API_COMPLETIONS_DEPLOYMENT_NAME="..."
   AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME="..."
   AZURE_OPENAI_API_VERSION="..."
   ```

2. Або ми можемо експортувати змінну середовища такою командою у вашу оболонку:

   2.1. Для Api OpenAI


   ```bash
   export OPENAI_API_KEY=sk-....
   ```

   2.2. Для Azure OpenAI:


   ```bash
   export AZURE_OPENAI_API_KEY="..."
   export AZURE_OPENAI_API_INSTANCE_NAME="..."
   export AZURE_OPENAI_API_DEPLOYMENT_NAME="..."
   export AZURE_OPENAI_API_COMPLETIONS_DEPLOYMENT_NAME="..."
   export AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME="..."
   export AZURE_OPENAI_API_VERSION="..."
   ```

3. Або ми можемо зробити це, коли ініціалізуємо обгортку разом з іншими аргументами. У цьому прикладі ми, ймовірно, хочемо, щоб виходи були більш випадковими, тому ми будемо ініціювати його з високою температурою.

   3.1. Для Api OpenAI


   ```typescript
   const model = new OpenAI({ openAIApiKey: "sk-...", temperature: 0.9 });
   ```

   3.2. Для Azure OpenAI:


   ```bash
   const model = new OpenAI({
     azureOpenAIApiKey: "...",
     azureOpenAIApiInstanceName: "....",
     azureOpenAIApiDeploymentName: "....",
     azureOpenAIApiVersion: "....",
     temperature: 0.9
   });
   ```

Після того, як ми ініціалізували обгортку, тепер ми можемо викликати його на деяких вхідних даних!


```typescript
const res = await model.call(
  "What would be a good company name a company that makes colorful socks?"
);
console.log(res);
```


```shell
{ res: '\n\nFantasy Sockery' }
```

### Шаблони підказок: керування підказками для LLM

Виклик LLM - це чудовий перший крок, але це лише початок. Зазвичай, коли ви використовуєте LLM в додатку, ви не надсилаєте введення користувача безпосередньо на LLM. Замість цього, ви, ймовірно, приймаєте користувацький ввід і будуєте підказку, а потім відправляєте його в LLM.

Наприклад, у попередньому прикладі текст, який ми передали, було важко закодовано, щоб попросити назву компанії, яка зробила барвисті шкарпетки. У цьому уявному сервісі ми б хотіли зробити тільки введення користувача, що описує те, що робить компанія, а потім форматувати підказку з цією інформацією.

Це легко зробити з LangChain!

Спочатку давайте визначимо шаблон запиту:


```typescript
import { PromptTemplate } from "langchain/prompts";

const template = "What is a good name for a company that makes {product}?";
const prompt = new PromptTemplate({
  template: template,
  inputVariables: ["product"],
});
```

Давайте тепер подивимося, як це працює! Ми можемо зателефонувати `.format` метод його форматування.


```typescript
const res = await prompt.format({ product: "colorful socks" });
console.log(res);
```


```shell
{ res: 'What is a good name for a company that makes colorful socks?' }
```

### Ланцюжки: об'єднуйте LLM та підказки в багатокрокових робочих процесах

До сих пір ми працювали з примітивами PromptTemplate і LLM самостійно. Але, звичайно, справжнє додаток - це не просто один примітивний, а скоріше їх комбінація.

Ланцюг у LangChain складається з посилань, які можуть бути або примітивами, такими як LLM, або іншими ланцюгами.

Найбільш основним типом ланцюга є LLMChain, який складається з PromptTemplate і LLM.

Розширюючи попередній приклад, ми можемо побудувати LLMChain, який приймає введення користувача, форматує його з PromptTemplate, а потім передає відформатовану відповідь на LLM.


```typescript
import { OpenAI } from "langchain/llms/openai";
import { PromptTemplate } from "langchain/prompts";

const model = new OpenAI({ temperature: 0.9 });
const template = "What is a good name for a company that makes {product}?";
const prompt = new PromptTemplate({
  template: template,
  inputVariables: ["product"],
});
```

Тепер ми можемо створити дуже простий ланцюжок, який прийме введення користувача, відформатує підказку з ним, а потім відправить його в LLM:


```typescript
import { LLMChain } from "langchain/chains";

const chain = new LLMChain({ llm: model, prompt: prompt });
```

Тепер ми можемо запустити цей ланцюжок тільки вказуючи продукт!


```typescript
const res = await chain.call({ product: "colorful socks" });
console.log(res);
```


```shell
{ res: { text: '\n\nColorfulCo Sockery.' } }
```

Ось так! Є перший ланцюжок - LLM Chain. Це один з простих типів ланцюгів, але розуміння того, як він працює, допоможе вам працювати з більш складними ланцюгами.

### Агенти: Динамічно запускаються ланцюжки на основі введення користувача

Поки що ланцюги, які ми розглядали, виконуються у заздалегідь визначеному порядку.

Агенти більше не роблять: вони використовують LLM, щоб визначити, які дії потрібно зробити і в якому порядку. Дія може або використовувати інструмент та спостерігати за його виводом, або повертатися до користувача.

При правильному використанні засоби можуть бути надзвичайно потужними. У цьому підручнику ми покажемо вам, як легко використовувати агенти через найпростіший, найвищий рівень API.

Для того, щоб завантажити агентів, ви повинні розуміти наступні поняття:

- Інструмент: Функція, яка виконує певну обов'язок. Це можуть бути такі речі, як: пошук Google, пошук бази даних, код REPL, інші ланцюжки. Інтерфейс інструменту в даний час є функцією, яка, як очікується, має рядок в якості вхідних даних, з рядком в якості виводу.
- LLM: Мовна модель живлення агента.
- Агент: Агент для використання. Це має бути рядок, що посилається на клас агента підтримки. Оскільки цей підручник фокусується на найпростішому, найвищому рівні API, це охоплює тільки з використанням стандартних підтримуваних агентів.

У цьому прикладі вам потрібно встановити змінні середовища SerpAPI в `.env` файл.


```bash
SERPAPI_API_KEY="..."
```

Встановити `serpapi` пакет (API пошуку Google):


```bash npm2yarn
npm install -S serpapi
```

Тепер ми можемо почати!


```typescript
import { OpenAI } from "langchain/llms/openai";
import { initializeAgentExecutorWithOptions } from "langchain/agents";
import { SerpAPI } from "langchain/tools";
import { Calculator } from "langchain/tools/calculator";

const model = new OpenAI({ temperature: 0 });
const tools = [
  new SerpAPI(process.env.SERPAPI_API_KEY, {
    location: "Austin,Texas,United States",
    hl: "en",
    gl: "us",
  }),
  new Calculator(),
];

const executor = await initializeAgentExecutorWithOptions(tools, model, {
  agentType: "zero-shot-react-description",
});
console.log("Loaded agent.");

const input =
  "Who is Olivia Wilde's boyfriend?" +
  " What is his current age raised to the 0.23 power?";
console.log(`Executing with input "${input}"...`);

const result = await executor.call({ input });

console.log(`Got output ${result.output}`);
```


```shell
langchain-examples:start: Executing with input "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?"...
langchain-examples:start: Got output Olivia Wilde's boyfriend is Jason Sudeikis, and his current age raised to the 0.23 power is 2.4242784855673896.
```

### Пам'ять: Додати стан до ланцюгів і агентів

Всі ланцюги та агенти, які ми пройшли, були без громадянства. Але часто, ви можете захотіти, щоб ланцюг або агент мав якесь поняття «пам'ять», щоб він міг запам'ятовувати інформацію про свої попередні взаємодії. Найяскравіший і простий приклад цього — це розробка чат-бота — ви хочете, щоб він запам’ятовував попередні повідомлення, щоб він міг використовувати контекст для кращої розмови. Це був би тип «короткочасної пам'яті». З більш складного боку, ви можете уявити собі ланцюжок / агент, що запам'ятовує ключові деталі інформації з плином часу - це буде форма «довготривалої пам'яті».

LangChain надає кілька спеціально створених ланцюжків саме для цієї мети. Цей розділ проходить за допомогою одного з цих ланцюгів ( `ConversationChain`).

За замовчуванням, `ConversationChain` має простий тип пам'яті, який запам'ятовує всі попередні входи/ виходи і додає їх в контекст, який передається. Давайте подивимося на використання цього ланцюга.


```typescript
import { OpenAI } from "langchain/llms/openai";
import { BufferMemory } from "langchain/memory";
import { ConversationChain } from "langchain/chains";

const model = new OpenAI({});
const memory = new BufferMemory();
const chain = new ConversationChain({ llm: model, memory: memory });
const res1 = await chain.call({ input: "Hi! I'm Jim." });
console.log(res1);
```


```shell
{response: " Hi Jim! It's nice to meet you. My name is AI. What would you like to talk about?"}
```


```typescript
const res2 = await chain.call({ input: "What's my name?" });
console.log(res2);
```


```shell
{response: ' You said your name is Jim. Is there anything else you would like to talk about?'}
```

## Потокове передавання

Ви також можете використовувати потокове API, щоб отримувати потокове передавання слів назад до вас, коли вони генеруються. Це корисно для, наприклад,. чат-ботів, де ви хочете, щоб показати користувачеві, що генерується, як вона генерується. Примітка: OpenAI з цього запису не підтримує `tokenUsage` звітування: увімкнуто потокове передавання.

<CodeBlock language="typescript">{Приклад}</CodeBlock>
