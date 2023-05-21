
Передумови [#](https://cactus.chat/docs/server/self-host/#prerequisites)
------------------------------------------------------------------------
Вам потрібно запустити власний домашній сервер Matrix.
[№](https://cactus.chat/docs/server/self-host/#configuration) конфігурації[](https://cactus.chat/docs/server/self-host/#configuration)
--------------------------------------------------------------------------------------------------------------------------------------
### Синапс [#](https://cactus.chat/docs/server/self-host/#synapse)
Створіть реєстраційний файл appservice `cactus.yaml`, який Synapse може читати. Використовуйте наступний шаблон і змініть маркери:
    # A unique, user-defined ID of the application service which will never change.
    id: "Cactus Comments"
    
    # Where the cactus-appservice is hosted:
    url: "http://cactus:5000"
    
    # Unique tokens used to authenticate requests between our service and the
    # homeserver (and the other way). Use the sha256 hashes of something random.
    # CHANGE THESE VALUES.
    as_token: "a2d7789eedb3c5076af0864f4af7bef77b1f250ac4e454c373c806876e939cca"
    hs_token: "b3b05236568ab46f0d98a978936c514eac93d8f90e6d5cd3895b3db5bb8d788b"
    
    # User associated with our service. In this case "@cactusbot:example.com"
    sender_localpart: "cactusbot"
    
    namespaces:
      aliases:
        - exclusive: true
          regex: "#comments_.*"
    
Потім додайте шлях до файлу в Synapse `homeserver.yaml`:
    app_service_config_files:
      - "/path/to/cactus.yaml"
    
Щоб дозволити гостьові коментарі без входу користувачів, вам потрібно ввімкнути гостьову реєстрацію. Для цього `allow_guest_access: true`встановіть `homeserver.yaml`.

### Сервіс додатків Cactus Comments [#](https://cactus.chat/docs/server/self-host/#cactus-comments-application-service)
Служба програми Cactus Comments повністю налаштована за допомогою змінних середовища.
Ім'я
Вимагається?
опис
CACTUS\_HS\_TOKEN
Так
Маркер, який використовується для автентифікації домашнього сервера. Це має відповідати `hs_token`реєстраційному файлу YAML.
CACTUS\_AS\_TOKEN
Так
Маркер, який використовується для автентифікації служби програми на домашньому сервері. Це має відповідати `as_token`реєстраційному файлу YAML.
CACTUS\_HOMESERVER\_URL
Так
Повна URL-адреса домашнього сервера, на якому зареєстрована служба програми.
CACTUS\_USER\_ID
Так
Ідентифікатор користувача для інтерфейсу чат-бота. Це має базуватися на `sender_localpart`реєстраційному файлі YAML. Приклад: `@cactusbot:example.com`.
CACTUS\_NAMESPACE\_REGEX
Немає
Регулярний вираз для псевдонімів кімнат, якими керує служба програми. Це має збігатися з регулярним виразом у файлі YAML реєстрації. Приклад: `#_comments2_.*`.
CACTUS\_NAMESPACE\_PREFIX
Немає
Префікс псевдонімів кімнат, якими керує служба програми. Це має бути встановлено, лише якщо `CACTUS_NAMESPACE_REGEX`встановлено і воно має відповідати цьому. Приклад: 

`_comments_2`.
CACTUS\_REGISTRATION\_REGEX
Немає
Для реєстрації нових сайтів дозволяйте лише ідентифікатори користувачів, які відповідають цьому регулярному виразу. приклад:

`@user1:example.org|@user2:example.org`
`CACTUS_NAMESPACE_REGEX`і `CACTUS_NAMESPACE_PREFIX`

існує на випадок, якщо ви хочете змінити регулярний вираз псевдоніма кімнати, яким керує служба програми. Це корисно, якщо ви хочете запустити кілька розгортань Cactus Comments на одному домашньому сервері.
Є чотири обов’язкові змінні середовища, і вони мають збігатися з визначеними вище `cactus.yaml`:
    CACTUS_HS_TOKEN=b3b05236568ab46f0d98a978936c514eac93d8f90e6d5cd3895b3db5bb8d788b
    CACTUS_AS_TOKEN=a2d7789eedb3c5076af0864f4af7bef77b1f250ac4e454c373c806876e939cca
    CACTUS_HOMESERVER_URL=http://synapse:8008
    CACTUS_USER_ID=@cactusbot:example.com
    
Запуск cactus-appservice [#](https://cactus.chat/docs/server/self-host/#running-cactus-appservice)
--------------------------------------------------------------------------------------------------
Наразі `cactus-appservice`в основному [поширюється як образ докера](https://hub.docker.com/r/cactuscomments/cactus-appservice) . Однак ви можете запустити його як службу systemd, клонувавши репо, за рахунок деяких додаткових кроків налаштування.
Служба програми не має статусу в будь-якому випадку.
### Використання докера [#](https://cactus.chat/docs/server/self-host/#using-docker)
Якщо наведені вище змінні середовища були визначені в `cactus.env`, ви могли б запустити службу програми безпосередньо за допомогою докера, наприклад:
    $ docker run --env-file cactus.env --name cactus cactuscomments/cactus-appservice:latest
    
У `docker-compose`, ця послуга може виглядати так:
    services:
      cactus:
        image: cactuscomments/cactus-appservice:latest
        env_file: "cactus.env"