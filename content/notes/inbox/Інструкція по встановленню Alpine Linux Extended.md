

Ця інструкція допоможе встановити Alpine Linux Extended на фізичному комп'ютері (не на віртуальній машині). Ми також налаштуємо доступ до системи через SSH та Cloudflared.

## Вимоги

- Комп'ютер, на якому ви плануєте встановити Alpine Linux
- USB-накопичувач для встановлення Alpine Linux

## Крок 1: Завантажте Alpine Linux

1. Відвідайте [офіційний сайт Alpine Linux](https://alpinelinux.org/downloads/) і завантажте Alpine Linux Extended.
2. Створіть завантажувальний USB-накопичувач, використовуючи програму, наприклад [Rufus](https://rufus.ie/) (Windows) або [Etcher](https://www.balena.io/etcher/) (Windows, macOS, Linux).

## Крок 2: Встановлення Alpine Linux

1. Вставте USB-накопичувач у комп'ютер, на якому потрібно встановити Alpine Linux.
2. Завантажте комп'ютер з USB-накопичувача.
3. Після завантаження ви побачите привітальний екран Alpine Linux. Введіть наступну команду для запуску налаштування:

   ```
   setup-alpine
   ```

4. Слідуйте інструкціям на екрані, вибираючи потрібні параметри мережі, клавіатури, та інші налаштування.
5. Під час налаштування дисків, виберіть опцію "sys" для встановлення Alpine Linux на жорсткий диск комп'ютера.
6. Завершіть процес налаштування та перезавантажте комп'ютер.

## Крок 3: Налаштування SSH

1. Залогіньтеся в систему та встановіть пакет `openssh`:

   ```
   apk add openssh
   ```

2. Відредагуйте файл `/etc/ssh/sshd_config` та внесіть наступні зміни:

   ```
   PermitRootLogin yes
   PasswordAuthentication yes
   ```

3. Запустіть SSH-сервер та додайте його до автозапуску:

   ```
   rc-service sshd start
   rc-update add sshd
   ```

## Крок 4: Встановлення та налаштування Cloudflared

1. Встановіть пакет `cloudflared`:

   ```
   apk add cloudflared
   ```

2. Зареєструйте новий тунель Cloudflare:

   ```
   cloudflared tunnel login
   ```

   Ця команда відкриє веб-сторінку в вашому браузері. Увійдіть у свій обліковий запис Cloudflare та дозвольте доступ до обраного домену.

3. Створіть файл конфігурації `/etc/cloudflared/config.yml` з наступним вмістом:

   ``` yaml
   tunnel: TUNNEL_ID
   credentials-file: /etc/cloudflared/TUNNEL_ID.json
   ingress:
     - hostname: example.com
       service: ssh://localhost:22
     - service: http_status:404
   ```

   Замініть `TUNNEL_ID` на ідентифікатор тунелю, який ви отримали на попередньому кроці, та `example.com` на ваш домен.

4. Запустіть сервіс `cloudflared` та додайте його до автозапуску:

   ```
   rc-service cloudflared start
   rc-update add cloudflared
   ```

Тепер ви повинні мати можливість доступу до вашої системи Alpine Linux через SSH та Cloudflared, використовуючи ваш домен. Використовуйте команду `ssh user@example.com` для доступу до системи, де `user` - ваш користувач на Alpine Linux, а `example.com` - ваш домен.