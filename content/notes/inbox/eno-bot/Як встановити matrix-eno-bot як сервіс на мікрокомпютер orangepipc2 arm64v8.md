

✅ Відповідь Всезнайки:

Привіт! Для того, щоб встановити matrix-eno-bot на мікрокомп'ютер Orange Pi PC2 з архітектурою arm64v8, вам спочатку потрібно встановити деякі залежності.

1. Спочатку встановіть Node.js та npm, якщо вони ще не встановлені на вашому пристрої. Ви можете встановити їх за допомогою наступних команд:

sudo apt-get update
sudo apt-get install nodejs npm


2. Потім встановіть Git, якщо він ще не встановлений, за допомогою наступної команди:

sudo apt-get install git


3. Після цього склонуйте репозиторій matrix-eno-bot за допомогою Git:

git clone https://github.com/8go/matrix-eno-bot.git


4. Перейдіть до папки з проектом і встановіть залежності за допомогою npm:

cd matrix-eno-bot
npm install


5. Потім ви можете запустити бота за допомогою команди:

npm start


Якщо ви хочете, щоб бот запускався автоматично при завантаженні пристрою, ви можете налаштувати його як службу за допомогою systemd. Для цього створіть файл конфігурації служби за допомогою команди:

sudo nano /etc/systemd/system/matrix-eno-bot.service


Вставте наступний текст у файл конфігурації:

[Unit]
Description=Matrix Eno Bot
After=network.target

[Service]
WorkingDirectory=/повний/шлях/до/matrix-eno-bot
ExecStart=/usr/bin/npm start
Restart=always
User=користувач
Group=група

[Install]
WantedBy=multi-user.target


Замініть /повний/шлях/до/matrix-eno-bot на повний шлях до папки з проектом, а користувач та група на користувача та групу, відповідно, які ви хочете використовувати для запуску бота.

Збережіть файл та запустіть команди:

sudo systemctl daemon-reload
sudo systemctl enable matrix-eno-bot.service
sudo systemctl start matrix-eno-bot.service


Тепер бот буде запускатися автоматично при завантаженні пристрою.

✅ Відповідь Chatgpt:

Для встановлення `matrix-eno-bot` як сервісу на мікрокомп'ютері `orangepipc2` з архітектурою `arm64v8`, необхідно виконати наступні кроки:

1.  Встановіть залежності
    
    Відкрийте термінал на мікрокомп'ютері та виконайте наступну команду, щоб встановити всі необхідні залежності:
    
    ```
    sudo apt-get update && sudo apt-get install -y nodejs npm git
    
    ```
    
    Ця команда оновить список пакетів та встановить необхідні пакети.
    
2.  Клонуйте репозиторій
    
    Клонуйте репозиторій `matrix-eno-bot` з GitHub, виконавши наступну команду:
    
    ```
    git clone https://github.com/8go/matrix-eno-bot.git
    
    ```
    
3.  Встановіть залежності проекту
    
    Перейдіть до папки з проектом, виконавши наступну команду:
    
    Потім встановіть залежності, виконавши команду:
    
    Ця команда встановить всі залежності проекту.
    
4.  Налаштуйте сервіс
    
    Створіть конфігураційний файл сервісу, виконавши команду:
    
    ```
    cp config.sample.js config.js
    
    ```
    
    Відкрийте файл `config.js` у текстовому редакторі та налаштуйте його для свого середовища. Наприклад, додайте свій URL-адрес та інші налаштування.
    
5.  Створіть файл служби
    
    Створіть файл служби для запуску `matrix-eno-bot` як сервісу, виконавши команду:
    
    ```
    sudo nano /etc/systemd/system/matrix-eno-bot.service
    
    ```
    
    Додайте наступний текст до цього файлу:
    
    ```
    [Unit]
    Description=matrix-eno-bot
    After=network.target
    
    [Service]
    Type=simple
    ExecStart=/usr/bin/node /повний/шлях/до/matrix-eno-bot/index.js
    WorkingDirectory=/повний/шлях/до/matrix-eno-bot/
    Restart=on-failure
    User=пользователь
    
    [Install]
    WantedBy=multi-user.target
    
    ```
    
    Замініть `/повний/шлях/до/matrix-eno-bot/` на шлях до папки з проектом \`matrix-eno


