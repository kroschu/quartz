

Встановлення Termux та віджету Termux
-----------------------------------------------------------------------

З Github Termux ,\[^1\] Github Termux Widget \[^2\] завантажте APK і встановіть їх. Ви також можете використовувати F-Droid.

Дайте Termux доступ до вашого сховища за допомогою наступної команди :\[^3\]

    termux-setup-storage
    

Налаштування Git та Github для роботи зі сховищами
-----------------------------------------------------------------------------------------------------------

￼Використовуйте наступні команди для налаштування git та github через HTTPS :

    pkg update && pkg upgrade
    

    pkg install git
    

    pkg install gh
    

_Ви також можете використовувати SSH_.

￼Увійдіть до свого облікового запису Github :

    gh auth login
    

￼Оновіть конфіги git'а :

\[^9\]: [Посібник для початківців про завдання Cron - OSTechNix](https://ostechnix.com/a-beginners-guide-to-cron-jobs/).
Translated with DeepL https://www.deepl.com/app/?utm_source=android&utm_medium=app&utm_campaign=share-translation