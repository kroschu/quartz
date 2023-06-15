Для створення Docker-контейнера і `docker-compose.yml` файлу для DrakonHub, спочатку створимо `Dockerfile`. Створіть файл з назвою `Dockerfile` у вашій робочій директорії з наступним вмістом:

```Dockerfile
# Use the official Tarantool image as the base
FROM tarantool/tarantool:2.x

# Install required dependencies
RUN apk update && \
    apk add luarocks wget unzip git cmake expat-dev build-base && \
    luarocks install luautf8 && \
    luarocks install luaexpat

# Download the latest DrakonHub build
WORKDIR /dewt
RUN wget https://drakonhub.com/files/latest-build.zip && \
    unzip /latest-build.zip && \
    rm /latest-build.zip

# Install Tarantool MySQL connector
WORKDIR /tmp
RUN git clone https://github.com/tarantool/mysql.git tarantool-mysql && \
    cd tarantool-mysql && \
    cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo && \
    make && \
    make install

# Copy the onprem.lua configuration file to the instances directory
COPY onprem.lua /etc/tarantool/instances.available/

# Create a symlink for the onprem.lua configuration file
RUN ln -s /etc/tarantool/instances.available/onprem.lua /etc/tarantool/instances.enabled/

# Expose the default DrakonHub port
EXPOSE 8090

# Start the DrakonHub instance
CMD ["tarantoolctl", "start", "onprem"]
```

Тепер створимо файл `onprem.lua` в тій же директорії, де знаходиться `Dockerfile`. Вставте наступний вміст, замінивши `my_site` на ваш IP-адресу або домен:

```lua
-- onprem.lua
box.cfg {
    listen = 3301
}

local work_dir = "/dewt/app"
package.path = package.path .. ';' .. work_dir .. '/?.lua;' .. work_dir .. '/?/init.lua'

require("global_cfg")
global_cfg.base_path = work_dir
global_cfg.scripts_path = work_dir .. "/scripts"

global_cfg.mg = false
global_cfg.emails_dir = "/dewt/emails"

local app = require("app")
app.init()

my_site = "my_site"

app.default_cfg(my_site)
```

Замініть `my_site` на вашу IP-адресу або доменне ім'я.

Тепер створимо файл `docker-compose.yml` в тій же директорії, де знаходиться `Dockerfile`. Вставте наступний вміст:

```yaml
version: "3.8"
services:
  drakonhub:
    build: .
    ports:
      - "8090:8090"
    volumes:
      - ./emails:/dewt/emails
```

Тепер можна створити Docker-образ, виконавши наступну команду в директорії з файлами `Dockerfile`, `onprem.lua` і `docker-compose.yml`:

```
docker-compose build
```

Після цього запустіть DrakonHub, виконавши наступну команду:

```
docker-compose up
```

DrakonHub тепер буде доступний у вашому веб-переглядачі за адресою `http://your-host-name:8090`.

Адміністратор: admin
Пароль: drakon