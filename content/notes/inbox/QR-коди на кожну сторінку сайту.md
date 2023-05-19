
В файлі шаблону header.html  наступного вмісту:
  ``` HTML
  
<header>
    {{ $config := cond (eq $.Site.Language.Lang "en") "config" (printf "config.%s" $.Site.Language.Lang) }}
    <img class="qr-code" src="https://chart.googleapis.com/chart?chs=90x90&amp;cht=qr&amp;chl=https://treba.m-e.pp.ua/{{ trim .Page.RelPermalink "/"}}&amp;chco=6B879A|FAF8F8" alt="QR Code">
    <div class="spacer"></div>
    <h1 id="page-title"><a class="root-title" href="{{ "" | absLangURL }}">{{ ( index $.Site.Data $config ).page_title | default $.Site.Data.config.page_title }}</a></h1>
    <div class="spacer"></div>
    <div id="search-icon">
        <p>{{ i18n "search" }}</p>
        <svg tabindex="0" aria-labelledby="title desc" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 19.9 19.7">
            <title id="title">{{ i18n "search_icon" }}</title>
            <desc id="desc">{{ i18n "icon_search" }}</desc>
            <g class="search-path" fill="none">
                <path stroke-linecap="square" d="M18.5 18.3l-5.4-5.4"/>
                <circle cx="8" cy="8" r="7"/>
            </g>
        </svg>
    </div>
    {{ partial "darkmode.html" .}}
  </header>
```

 Вже додано QR - код :

 `<img class="qr-code" src="https://chart.googleapis.com/chart?chs=90x90&amp;cht=qr&amp;chl=https://treba.m-e.pp.ua/{{ trim .Page.RelPermalink "/"}}&amp;chco=6B879A|FAF8F8" alt="QR Code">`

Цей код є HTML-тегом для вставки QR-коду на веб-сторінку. Він використовує зовнішній зображення QR-коду, отримане з сервісу Google Charts API.

Основний HTML-тег у коді це `<img>`, який відповідає за відображення зображення на сторінці. В атрибуті `class` має значення `"qr-code"`, це дозволяє задати стилі для зображення за допомогою CSS.

Атрибут `src` вказує на джерело зображення QR-коду. В даному випадку, він містить посилання на URL-адресу `https://chart.googleapis.com/chart?chs=90x90&amp;cht=qr&amp;chl=https://treba.m-e.pp.ua/{{ trim .Page.RelPermalink "/"}}&amp;chco=6B879A|FAF8F8`. Цей URL-адрес передає параметри до сервісу Google Charts API, щоб створити QR-код.

Параметри у URL-адресі пояснюються наступним чином:
- `chs=90x90` - розміри зображення QR-коду (90 пікселів у висоту та ширину).
- `cht=qr` - тип зображення (QR-код).
- `chl=https://treba.m-e.pp.ua/{{ trim .Page.RelPermalink "/"}}` - дані, які будуть закодовані в QR-коді. Вони складаються з URL-адреси `https://treba.m-e.pp.ua/` та шляху до поточної сторінки (`.Page.RelPermalink`). Функція `trim` використовується для видалення символів `/` з початку та кінця шляху.
- `chco=6B879A|FAF8F8` - кольори QR-коду. В даному випадку, квадратики коду матимуть кольори `#6B879A` (темно-сірий) та `#FAF8F8` (світло-сірий).

Таким чином, на сторінці буде відображатись зображення QR-коду, яке буде містити закодовану URL-адресу `https://treba.m-e.pp.ua/` разом із шляхом до поточної сторінки.