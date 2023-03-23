---
title: "docker"
---

Якщо ви хочете розмістити Quartz на машині без використання хостингу веб-сторінок, може бути простіше [встановити Docker Compose](https://docs.docker.com/compose/install/) і слідувати наведеним нижче інструкціям, ніж [встановлювати залежності Quartz вручну](Перегляд%20змін.md).
### Локальний хостинг Quartz
Ви можете розмістити Quartz локально за адресою `http://localhost:1313` за допомогою наступного скрипта, замінивши `/path/to/quartz` на
фактичним шляхом до вашої теки Quartz.

docker-compose.yml
```
services:
  quartz-hugo:
    image: ghcr.io/jackyzha0/quartz:hugo
    назва_контейнера: quartz-hugo
    томи:
      - /path/to/quartz:/quartz
    порти:
      - 1313:1313

    # необов'язково
    оточення:
      - HUGO_BIND=0.0.0.0
      - HUGO_BASEURL=http://localhost
      - HUGO_PORT=1313
      - HUGO_APPENDPORT=true
      - HUGO_LIVERELOADPORT=-1
```

Потім запустіть з: `docker-compose up -d` у тому ж каталозі, де знаходиться ваш файл `docker-compose.yml`.

Поки контейнер працює, ви можете оновити форк `quartz` за допомогою: `docker exec -it quartz-hugo make update`.

## Оприлюднення вашого контейнера в інтернеті
### На вашу публічну IP-адресу з переадресацією портів (небезпечно)

Припускаємо, що ви вже знайомі з [переадресацією портів](https://en.wikipedia.org/wiki/Port_forwarding) і [налаштуванням її на вашій моделі роутера](https://portforward.com):

1. Встановіть змінну оточення `HUGO_BASEURL=http://your-public-ip` і запустіть ваш контейнер.
2. Налаштуйте перенаправлення портів на вашому роутері з порту `p` на `your-local-ip:1313`.
3. Тепер ви зможете отримати доступ до Quartz з-за меж вашої локальної мережі за адресою `http://your-public-ip:p`.

Однак, ваше HTTP-з'єднання буде незашифрованим і **цей метод не є безпечним**.

### До домену за допомогою проксі Cloudflare

1. Переадресуйте порт 443 (HTTPS) зі свого комп'ютера.
2. Придбайте власний домен (наприклад, `your-domain.com`) у [Cloudflare] (https://www.cloudflare.com/products/registrar/). Перенаправте запис DNS A з `your-domain.com` на вашу публічну IP-адресу та увімкніть проксі.
3. Встановіть змінні оточення `HUGO_BASEURL=https://your-domain.com`, `HUGO_PORT=443` та `HUGO_APPENDPORT=false`. Замініть `1313:1313` на `443:443` для `ports` у файлі `docker-compose.yml`.
4. Запускайте свій Quartz-контейнер і насолоджуйтеся ним на `https://your-domain.com`!

### До домену за допомогою зворотного проксі

Якщо ви хочете обслуговувати на цій машині не тільки Quartz (або не хочете використовувати реєстратор і проксі Cloudflare), вам слід виконати кроки, описані в розділі вище (за необхідності), а також налаштувати зворотний проксі, наприклад, [Traefik] (https://doc.traefik.io/traefik). Не забудьте також налаштувати сертифікати TLS!