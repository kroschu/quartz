
import CodeBlock from "@theme/CodeBlock";

Оскільки Upstash Redis працює через REST API, ви можете використовувати його з [Vercel Edge](https://vercel.com/docs/concepts/functions/edge-functions/edge-runtime), [Cloudflare Workers](https://developers.cloudflare.com/workers/) та іншими безсерверними середовищами.
На основі чат-пам'яті з підтримкою Redis.

Для більш тривалого збереження даних у чаті ви можете замінити стандартний клас пам'яті `chatHistory`, який підтримує класи пам'яті чату, такі як `BufferMemory`, на екземпляр Upstash [Redis](https://redis.io/)￼.

￼## Налаштування

You will need to install [@upstash/redis](https://github.com/upstash/upstash-redis) in your project:

```bash npm2yarn
npm install @upstash/redis
```

You will also need an Upstash Account and a Redis database to connect to. See instructions on [Upstash Docs](https://docs.upstash.com/redis) on how to create a HTTP client.

## Usage

Кожен сеанс історії чату, що зберігається в Redis, повинен мати унікальний ідентифікатор. Ви можете вказати необов'язковий параметр sessionTT, щоб сесії завершувалися через певну кількість секунд.
Параметр config передається безпосередньо у new Redis()конструктор@upstash/redis і приймає ті самі аргументи.
<CodeBlock language="typescript">{Example}</CodeBlock>

## Advanced Usage

You can also directly pass in a previously created [@upstash/redis](https://docs.upstash.com/redis/sdks/javascriptsdk/overview) client instance:

import AdvancedExample from "@examples/memory/upstash_redis_advanced.ts";

<CodeBlock language="typescript">{AdvancedExample}</CodeBlock>
