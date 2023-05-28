

імпорт CodeBlock з «@theme/CodeBlock»; імпорт прикладу з «@examples/models/chat/chat_streaming_stdout.ts»;

Чат-моделі - це різновид мовних моделей. У той час як моделі чату використовують мовні моделі під капотом, інтерфейс, який вони надають, трохи відрізняється. Замість того, щоб викрити API «текст у, текст назовні», вони надають інтерфейс, де «повідомлення чату» є вхідними та вихідними даними.

Чат моделі API є досить новими, тому ми все ще з'ясовуємо правильні абстракції.

## Інсталяція та настроювання

Щоб почати роботу, виконайте наведені нижче дії. [інструкції з інсталяції](./install) щоб встановити LangChain.

## Початок роботи

У цьому розділі описано, як почати роботу з моделями чату. Інтерфейс базується на повідомленнях, а не на необробленому тексті.


```typescript
import { ChatOpenAI } from "langchain/chat_models/openai";
import { HumanChatMessage, SystemChatMessage } from "langchain/schema";

const chat = new ChatOpenAI({ temperature: 0 });
```

Тут ми створюємо модель чату за допомогою ключа API, що зберігається в змінній середовища `OPENAI_API_KEY` або `AZURE_OPENAI_API_KEY` у випадку, якщо ви використовуєте Azure OpenAI. Ми телефонуватимемо цій моделі чату в цьому розділі.

> **&#9432;** Примітка, якщо ви використовуєте Azure OpenAI переконайтеся, що також встановити змінні середовища `AZURE_OPENAI_API_INSTANCE_NAME`, `AZURE_OPENAI_API_DEPLOYMENT_NAME` і `AZURE_OPENAI_API_VERSION`.

### Моделі чатів: повідомлення, повідомлення

Ви можете отримати завершення чату, передаючи одне або кілька повідомлень моделі чату. У відповідь також буде з'являтися повідомлення. Типи повідомлень, які в даний час підтримуються в LangChain є `AIChatMessage`, `HumanChatMessage`, `SystemChatMessage`, а також загальний `ChatMessage` — ChatMessage приймає довільний параметр ролі, який ми тут не використовуватимемо. Більшу частину часу, ви будете мати справу з `HumanChatMessage`, `AIChatMessage`, і `SystemChatMessage`.


```typescript
const response = await chat.call([
  new HumanChatMessage(
    "Translate this sentence from English to French. I love programming."
  ),
]);

console.log(response);
```


```
AIChatMessage { text: "J'aime programmer." }
```

#### Кілька повідомлень

Чат-моделі OpenAI (в даний час `gpt-3.5-turbo` і `gpt-4` і у випадку з azure OpenAI `gpt-4-32k`) підтримує декілька повідомлень як вхідні дані. Див. [here](https://platform.openai.com/docs/guides/chat/chat-vs-completions) для отримання додаткової інформації. Ось приклад відправки системного і користувальницького повідомлення в модель чату:

> **&#9432;** Примітка. Якщо використовується Azure OpenAI, переконайтеся, що ім’я розгортання змінено на розгортання для вибраної моделі.


```typescript
const responseB = await chat.call([
  new SystemChatMessage(
    "You are a helpful assistant that translates English to French."
  ),
  new HumanChatMessage("Translate: I love programming."),
]);

console.log(responseB);
```


```
AIChatMessage { text: "J'aime programmer." }
```

#### Багаторазові завершення

Ви можете йти на один крок далі і створювати доповнення для декількох наборів повідомлень за допомогою генерування. Це повертає результат з додатковим параметром повідомлення.


```typescript
const responseC = await chat.generate([
  [
    new SystemChatMessage(
      "You are a helpful assistant that translates English to French."
    ),
    new HumanChatMessage(
      "Translate this sentence from English to French. I love programming."
    ),
  ],
  [
    new SystemChatMessage(
      "You are a helpful assistant that translates English to French."
    ),
    new HumanChatMessage(
      "Translate this sentence from English to French. I love artificial intelligence."
    ),
  ],
]);

console.log(responseC);
```


```
{
  generations: [
    [
      {
        text: "J'aime programmer.",
        message: AIChatMessage { text: "J'aime programmer." },
      }
    ],
    [
      {
        text: "J'aime l'intelligence artificielle.",
        message: AIChatMessage { text: "J'aime l'intelligence artificielle." }
      }
    ]
  ]
}
```

### Шаблони підказок чату: керування підказками для моделей чату

Ви можете використовувати шаблон, використовуючи `MessagePromptTemplate`. Ви можете побудувати `ChatPromptTemplate` від одного або декількох `MessagePromptTemplates`. Ви можете використовувати `ChatPromptTemplate` с `formatPromptValue` — це повертає a `PromptValue`, який можна перетворити на рядок або об’єкт Message, залежно від того, чи слід використовувати форматоване значення як вхідні дані до моделі llm або chat.

Продовжуючи з попереднім прикладом:


```typescript
import {
  SystemMessagePromptTemplate,
  HumanMessagePromptTemplate,
  ChatPromptTemplate,
} from "langchain/prompts";
```

Спочатку створюємо багаторазовий шаблон:


```typescript
const translationPrompt = ChatPromptTemplate.fromPromptMessages([
  SystemMessagePromptTemplate.fromTemplate(
    "You are a helpful assistant that translates {input_language} to {output_language}."
  ),
  HumanMessagePromptTemplate.fromTemplate("{text}"),
]);
```

Потім ми можемо використовувати шаблон для створення відповіді:


```typescript
const responseA = await chat.generatePrompt([
  await translationPrompt.formatPromptValue({
    input_language: "English",
    output_language: "French",
    text: "I love programming.",
  }),
]);

console.log(responseA);
```


```
{
  generations: [
    [
      {
        text: "J'aime programmer.",
        message: AIChatMessage { text: "J'aime programmer." }
      }
    ]
  ]
}
```

### Модель + Запит = LLMChain

Такий шаблон прохання про завершення форматованої підказки досить поширений, тому представляємо наступний фрагмент пазла: LLMChain


```typescript
const chain = new LLMChain({
  prompt: translationPrompt,
  llm: chat,
});
```

Далі можна назвати ланцюжок:


```typescript
const responseB = await chain.call({
  input_language: "English",
  output_language: "French",
  text: "I love programming.",
});

console.log(responseB);
```


```
{ text: "J'aime programmer." }
```

### Агенти: Динамічно запускаються ланцюжки на основі введення користувача

Нарешті, ми представляємо інструменти та агенти, які розширюють модель з іншими можливостями, такими як пошук, або калькулятор.

Інструмент — це функція, яка приймає рядок (наприклад, пошуковий запит) і повертає рядок (наприклад, результат пошуку). Вони також мають назву та опис, які використовуються моделлю чату для визначення того, який інструмент він повинен викликати.


```typescript
class Tool {
  name: string;
  description: string;
  call(arg: string): Promise<string>;
}
```

Агент — це обгортка без громадянства навколо ланцюжка запитів агента (такого як MRKL), який піклується про інструменти форматування в запит, а також розбору відповідей, отриманих з моделі чату.


```typescript
interface AgentStep {
  action: AgentAction;
  observation: string;
}

interface AgentAction {
  tool: string; // Tool.name
  toolInput: string; // Tool.call argument
}

interface AgentFinish {
  returnValues: object;
}

class Agent {
  plan(steps: AgentStep[], inputs: object): Promise<AgentAction | AgentFinish>;
}
```

Для того, щоб зробити агенти більш потужними, ми повинні зробити їх ітеративними, тобто. називати модель кілька разів, поки вони не дійдуть до остаточної відповіді. Це робота АгентаВиконавця.


```typescript
class AgentExecutor {
  // a simplified implementation
  run(inputs: object) {
    const steps = [];
    while (true) {
      const step = await this.agent.plan(steps, inputs);
      if (step instanceof AgentFinish) {
        return step.returnValues;
      }
      steps.push(step);
    }
  }
}
```

І, нарешті, ми можемо використовувати AgentActor для запуску агента:


```typescript
// Define the list of tools the agent can use
const tools = [
  new SerpAPI(process.env.SERPAPI_API_KEY, {
    location: "Austin,Texas,United States",
    hl: "en",
    gl: "us",
  }),
];
// Create the agent from the chat model and the tools
const agent = ChatAgent.fromLLMAndTools(new ChatOpenAI(), tools);
// Create an executor, which calls to the agent until an answer is found
const executor = AgentExecutor.fromAgentAndTools({ agent, tools });

const responseG = await executor.run(
  "How many people live in canada as of 2023?"
);

console.log(responseG);
```


```
38,626,704.
```

### Пам'ять: Додати стан до ланцюгів і агентів

Ви також можете використовувати ланцюг для зберігання стану. Це корисно для, наприклад, чат-ботів, де ви хочете відстежувати історію розмов. MessagesPlaceholder - це спеціальний шаблон запиту, який буде замінено повідомленнями, переданими під час кожного виклику.


```typescript
const chatPrompt = ChatPromptTemplate.fromPromptMessages([
  SystemMessagePromptTemplate.fromTemplate(
    "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."
  ),
  new MessagesPlaceholder("history"),
  HumanMessagePromptTemplate.fromTemplate("{input}"),
]);

const chain = new ConversationChain({
  memory: new BufferMemory({ returnMessages: true, memoryKey: "history" }),
  prompt: chatPrompt,
  llm: chat,
});
```

Ланцюг буде внутрішньо накопичувати повідомлення, відправлені в модель, і ті, які отримані в якості вихідних даних. Потім він буде вводити повідомлення в підказку на наступний дзвінок. Так ви зможете викликати ланцюжок кілька разів, і вона запам'ятовує попередні повідомлення:


```typescript
const responseH = await chain.call({
  input: "hi from London, how are you doing today",
});

console.log(responseH);
```


```
{
  response: "Hello! As an AI language model, I don't have feelings, but I'm functioning properly and ready to assist you with any questions or tasks you may have. How can I help you today?"
}
```


```typescript
const responseI = await chain.call({
  input: "Do you know where I am?",
});

console.log(responseI);
```


```
{
  response: "Yes, you mentioned that you are from London. However, as an AI language model, I don't have access to your current location unless you provide me with that information."
}
```

## Потокове передавання

Ви також можете використовувати потокове API, щоб отримувати потокове передавання слів назад до вас, коли вони генеруються. Це корисно для, наприклад,. чат-ботів, де ви хочете, щоб показати користувачеві, що генерується, як вона генерується. Примітка: OpenAI з цього запису не підтримує `tokenUsage` звітування: увімкнуто потокове передавання.

<CodeBlock language="typescript">{Приклад}</CodeBlock>
