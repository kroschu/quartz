Для додавання дописів на Git Pages (Hugo, Perlite project) через вебхуки з використанням Typebot, спочатку потрібно встановити та налаштувати всі необхідні компоненти. Ось покрокова інструкція:

1. **Створіть новий репозиторій на GitHub** для Hugo проекту. Назвіть його, наприклад, `my-perlite-blog`. Склонуйте репозиторій на локальній машині.

2. **Встановіть Hugo** на вашій машині, якщо ви ще цього не зробили. Детальні інструкції можна знайти на [офіційному сайті Hugo](https://gohugo.io/getting-started/installing/).

3. **Створіть новий Hugo сайт** в репозиторії `my-perlite-blog`. Виконайте наступні команди:

   ````
   cd my-perlite-blog
   hugo new site .
   ```

4. **Додайте тему Perlite**. Знайдіть тему Perlite на GitHub, а потім додайте її як субмодуль в репозиторій:

   ````
   git submodule add https://github.com/YOUR_USERNAME/perlite.git themes/perlite
   ```

   Не забудьте замінити `YOUR_USERNAME` на ваше користувацьке ім'я на GitHub.

5. **Налаштуйте сайт Hugo**. Відкрийте файл `config.toml` в корені проекта і змініть налаштування, щоб він використовував тему Perlite:

   ```
   theme = "perlite"
   ```

6. **Створіть вебхук для Typebot**. Зареєструйтеся на [Typebot](https://www.typebot.io) і створіть новий вебхук. Вам потрібно вказати URL, на який будуть надіслані дані з форми. Наприклад, `https://your-hosting.com/webhook-receiver`.

7. **Додайте форму на ваш сайт**. Додайте HTML-код форми, що відправляє дані на ваш Typebot вебхук:

   ```
   <form action="https://your-hosting.com/webhook-receiver" method="POST">
       <label for="title">Назва:</label>
       <input type="text" id="title" name="title" required>
       <label for="content">Контент:</label>
       <textarea id="content" name="content" required></textarea>
       <button type="submit">Надіслати</button>
   </form>
   ```

8. **Створіть webhook-receiver**. На вашому власному хостингу створіть файл `webhook-receiver.php` (або інший файл відповідного типу, залежно від використовуваної мови програмування). В цьому файлі ви будете обробляти дані, надіслані з форми, і створювати нові дописи в Hugo.

9. **Обробка вебхуку**. В файлі `webhook-receiver.php` (або іншому) додайте код для обробки вебхука:

   - Витягніть дані з форми (назва допису та контент).
   - Створіть новий файл `.md` в каталозі `content/posts` з відповідними даними.
   - Збережіть зміни в репозиторії та надішліть їх на GitHub.
   - Запустіть команду `hugo` для генерації статичних сторінок сайту.

   Ось приклад коду на PHP:

   ``` php
   <?php
   // webhook-receiver.php

   $title = $_POST['title'];
   $content = $_POST['content'];

   $filename = 'content/posts/' . strtolower(str_replace(' ', '-', $title)) . '.md';

   $file_content = "---\ntitle: \"" . $title . "\"\ndate: " . date('Y-m-d') . "\n---\n\n" . $content;

   file_put_contents($filename, $file_content);

   exec('git add .');
   exec('git commit -m "Add new post: ' . $title . '"');
   exec('git push');

   exec('hugo');

   echo "New post added successfully.";
   ?>


   ```

10. **Настройте GitHub Pages**. У файлі `config.toml` додайте налаштування для публікації сайту на GitHub Pages:

    ```
    publishDir = "docs"
    ```

    Збережіть зміни, запустіть `hugo` та надішліть згенеровані файли на GitHub:

    ```
    git add .
    git commit -m "Configure GitHub Pages"
    git push
    ```

11. **Активуйте GitHub Pages**. Перейдіть у налаштування репозиторія на GitHub, знайдіть розділ "GitHub Pages" та активуйте його, вибравши гілку `main` (або `master`) та папку `/docs`. Збережіть зміни.

Тепер ваш Hugo сайт з темою Perlite опублікований на GitHub Pages, і ви можете додавати нові дописи, використовуючи форму на вашому сайті. Вебхук Typebot буде обробляти дані форми та автоматично створювати нові дописи на вашому сайті.