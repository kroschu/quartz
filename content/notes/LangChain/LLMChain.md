
імпорт CodeBlock з «@theme/CodeBlock»; імпорт ExampleLLM з «@examples/chains/llm_chain.ts»; імпорт ExampleChat з «@examples/chains/llm_chain_chat.ts»; імпорт ExampleStream з «@examples/chains/llm_chain_stream.ts»; імпорт ExampleCancellation з «@examples/chains/llm_chain_cancellation.ts»;

# Початок роботи:

:::інформація [Концептуальне керівництво](https://docs.langchain.com/docs/components/chains/llm-chain)
:::

Ан `LLMChain` це простий ланцюжок, який додає деякі функціональні можливості навколо мовних моделей. Він широко використовується по всьому лангЧейн, в тому числі в інших ланцюгах і агентів.

Ан `LLMChain` складається з `PromptTemplate` і модель мови (або [LLM](../models/llms/) або [chat model](../models/chat/)).

## Використання з LLM

Ми можемо побудувати LLMChain, який приймає введення користувача, форматує його з PromptTemplate, а потім передає відформатовану відповідь на LLM:

<CodeBlock language="typescript">{ПрикладLLM}</CodeBlock>

## Використання з моделями чату

Ми також можемо побудувати LLMChain, який приймає введення користувача, форматує його за допомогою PromptTemplate, а потім передає форматовану відповідь на ChatModel:

<CodeBlock language="typescript">{ПрикладЧату}</CodeBlock>

## Використання в режимі потокового передавання

Ми також можемо побудувати LLMChain, який приймає введення користувача, форматує його з PromptTemplate, а потім передає відформатовану відповідь на LLM в потоковому режимі, який буде передавати назад маркери, як вони генеруються:

<CodeBlock language="typescript">{ExampleStream}</CodeBlock>

## Скасування запущеного LLMChain

Також можна скасувати запуск LLMChain, передавши AbortSignal до `call` метод:

<CodeBlock language="typescript">{ПрикладСкасування}</CodeBlock>

У цьому прикладі ми показуємо скасування в потоковому режимі, але він працює так само в режимі без потокового передавання.
