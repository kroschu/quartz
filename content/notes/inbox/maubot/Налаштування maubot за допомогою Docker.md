---
title: "Налаштування maubot за допомогою Docker"
---

[Налаштування за допомогою Docker](https://docs.mau.fi/maubot/usage/setup/docker.html#setup-with-docker)

Зображення Docker розміщені на [dock.mau.dev](https://mau.dev/maubot/maubot/container_registry)

0.  Створіть каталог ( `mkdir maubot`) і введіть його ( `cd maubot`).
1.  Витягніть зображення докера за допомогою `docker pull dock.mau.dev/maubot/maubot:<version>`. Замініть `<version>`версією, яку хочете запустити (наприклад `latest`, )
2.  Запустіть контейнер уперше, щоб він міг створити файл конфігурації для вас:
    
    `docker run --rm -v $PWD:/data:z dock.mau.dev/maubot/maubot:<version>`
    
3.  Оновіть конфігурацію на свій смак.
4.  Запустіть maubot:
    
    `docker run --restart unless-stopped -p 29316:29316 -v $PWD:/data:z dock.mau.dev/maubot/maubot:<version>`
    
5.  Тепер інтерфейс керування має бути доступним за адресою [http://localhost:29316/\_matrix/maubot](http://localhost:29316/_matrix/maubot) або будь-яким іншим, що ви налаштували.

### [Оновлення](https://docs.mau.fi/maubot/usage/setup/docker.html#upgrading)

1.  Витягніть нову версію (крок налаштування 1).
2.  Перезапустіть контейнер.
