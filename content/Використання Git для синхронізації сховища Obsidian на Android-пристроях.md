---
title: "Використання Git для синхронізації сховища Obsidian на Android-пристроях"
---

[Джерело](https://forum.obsidian.md/c/share-showcase/9) 


1. Встановити Termux та Termux Widget
-----------------------------------------------------------------------

З Github Termux ,\[^1\] Github Termux Widget \[^2\] завантажте APK і встановіть їх. Ви також можете використовувати F-Droid.

Надайте Termux доступ до вашого сховища за допомогою наступної команди :\[^3\]

    termux-setup-storage
    

2. Налаштування Git і Github для роботи зі сховищами
-----------------------------------------------------------------------------------------------------------

Використовуйте наступні команди для налаштування git та github через HTTPS :

    pkg update && pkg upgrade
    

    pkg install git
    

    pkg install gh
    

Ви також можете використовувати SSH_.

Увійдіть до свого облікового запису Github :

    gh auth login
    

Оновлення конфігів git'а :

    git config --global user.name "name"
    

    git config --global user.email "email"
    

Тепер вам слід клонувати ваш репозиторій, спробуйте скористатися наступними командами :

    git status
    git pull
    git commit
    git push
    

Якщо ви використовуєте Android 12, ви отримаєте помилку при виконанні команди, яка вимагає додати сховище до списку безпеки або чогось подібного. Виконайте її, і ці команди повинні запрацювати.

3. Налаштувати ярлик сценарію синхронізації
-------------------------------------------------------------------

Створіть каталог для ярликів :\[^4\]

    mkdir -p /data/data/com.termux/files/home/.shortcuts
    chmod 700 -R /data/data/com.termux/files/home/.shortcuts
    mkdir -p /data/data/com.termux/files/home/.shortcuts/tasks
    chmod 700 -R /data/data/com.termux/files/home/.shortcuts/tasks
    

Створіть скрипт синхронізації :

    nano /data/data/com.termux/files/home/.shortcuts/tasks/sync_script.sh
    

Додайте наступний скрипт :\[^5\]

    #!/bin/bash
    cd storage/shared/LifeWiki
    git pull && git add -A && git commit -a -m "android vault backup: `date +'%Y-%m-%d %H-%M-%S'`" && git pull
    

Створіть віджет і додайте його на домашній екран. Ось і все, вам потрібно лише запустити його, щоб синхронізувати ваше сховище Obsidian. Це означає, що вам потрібно запускати його до і після редагування нотаток. Якщо ви помістили скрипт в ~/.shortcuts, він запуститься на передньому плані, а якщо в ~/.shortcuts/tasks, то у фоновому режимі. Я рекомендую використовувати як віджет той, який виконує код на передньому плані, а інший залишити для роботи Cron.

4. Налаштування автоматичного виконання скрипта
-----------------------------------------------------------------------------------------------------

Якщо ви хочете, наприклад, автоматично **синхронізувати ваше сховище щогодини**, ви можете зробити це за допомогою завдання Cron. \[^6\] \[^7\] \[^8\]

По-перше, вам потрібно встановити Cron :

    pkg install cronie termux-services
    

Після цього перезапустіть Termux і виконайте наступне :

    sv-enable crond
    crontab -e
    

Нарешті, ви отримаєте команду `crontab -e` у текстовому редакторі **nano**. Додайте наступний рядок :

    * */1 * * * bash ~/.shortcuts/tasks/sync_script.sh
    

Ви можете легко знайти інформацію про роботу Cron в інтернеті.\[^9\]


\[^1\]: [Як встановити Git на Android за допомогою Termux (покроковий посібник)](https://www.techrepublic.com/article/how-to-install-git-on-android/)

\[^2\]: [Мобільна синхронізація для Obsidian | Деякі думки](https://werzum.github.io/tech/2022/02/13/Obsidian-Mobile-Sync.html) та [Як синхронізувати сховище Obsidian на мобільному за допомогою git : ObsidianMD](https://www.reddit.com/r/ObsidianMD/comments/v6otbu/how_to_sync_your_obsidian_vault_on_mobile_using/)

\[^3\]: [Git Guides - git add - GitHub](https://github.com/git-guides/git-add) та [bash - Як встановити поточну дату як повідомлення git commit - Stack Overflow](https://stackoverflow.com/questions/4654437/how-to-set-current-date-as-git-commit-message)

\[^4\]: [Obsidian Syncing Alternative | Obsidian-Sync-Alternative](https://pulinagrawal.github.io/Obsidian-Sync-Alternative/)

\[^5\]: [Інтеграція Obsidian Github для синхронізації та контролю версій - Обмін та демонстрація - Форум Obsidian](https://forum.obsidian.md/t/obsidian-github-integration-for-sync-and-version-control/6369)

\[^6\]: [Obsidian Syncing Alternative | Obsidian-Sync-Alternative](https://pulinagrawal.github.io/Obsidian-Sync-Alternative/)

\[^7\]: [Інтеграція Obsidian Github для синхронізації та контролю версій - Ділимося та демонструємо - Форум Obsidian](https://forum.obsidian.md/t/obsidian-github-integration-for-sync-and-version-control/6369)

\[^8\]: [Посібник: Obsidian vault github sync cron на termux : ObsidianMD](https://www.reddit.com/r/ObsidianMD/comments/qep4gn/guide_obsidian_vault_github_sync_cron_on_termux/)

\[^9\]: [Посібник для початківців про завдання cron - OSTechNix](https://ostechnix.com/a-beginners-guide-to-cron-jobs/)