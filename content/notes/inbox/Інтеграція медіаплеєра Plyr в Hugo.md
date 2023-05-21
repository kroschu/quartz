Щоб інтегрувати медіаплеєр Plyr на сторінку сайту, згенерованого за допомогою Hugo, виконайте такі кроки:

1. Завантажте та підключіть файли Plyr:

   - Завантажте Plyr з GitHub: `git clone https://github.com/sampotts/plyr.git`
   - Скопіюйте файл `plyr/dist/plyr.min.css` в папку `static/css` вашого проекту Hugo.
   - Скопіюйте файл `plyr/dist/plyr.min.js` в папку `static/js` вашого проекту Hugo.

2. Підключіть файли стилів та скриптів Plyr до вашої сторінки:

   Відкрийте файл шаблону HTML, який використовується для сторінки, де ви хочете підключити Plyr (наприклад, `layouts/_default/baseof.html`). Додайте наступний код:

   ````html
   <link rel="stylesheet" href="/css/plyr.min.css">
   ```

   Вставте цей рядок у секцію `<head>` вашого HTML-файлу.

   Тепер додайте наступний код перед закриттям тега `</body>`:

   ````html
   <script src="/js/plyr.min.js"></script>
   <script>
     document.addEventListener('DOMContentLoaded', function () {
       const player = new Plyr('video, audio');
     });
   </script>
   ```

3. Додайте HTML-код медіаплеєра Plyr на вашу сторінку:

   Відкрийте файл з вмістом сторінки, де ви хочете додати медіаплеєр (наприклад, `content/post/my-post.md`). Додайте наступний код:

   Для відео:

   ````html
   <div class="plyr__video-embed">
     <video controls crossorigin>
       <source src="path/to/your/video.mp4" type="video/mp4">
       Ваш браузер не підтримує відео.
     </video>
   </div>
   ```

   Для аудіо:

   ````html
   <div class="plyr__audio-embed">
     <audio controls crossorigin>
       <source src="path/to/your/audio.mp3" type="audio/mp3">
       Ваш браузер не підтримує аудіо.
     </audio>
   </div>
   ```

   Замініть `path/to/your/video.mp4` та `path/to/your/audio.mp3` на відповідні шляхи до вашого відео та аудіо.

4. Запустіть ваш проект Hugo і перевірте результат:

   У командному рядку введіть `hugo server` та відкрийте ваш сайт в браузері за адресою `http://localhost:1313`. Перейдіть на сторінку, де ви додали медіаплеєр Plyr, і переконайтеся, що відео та аудіо працюють належним чином.

Тепер медіаплеєр Plyr успішно інтегрований на вашу сторінку сайту, згенеровану за допомогою Hugo.