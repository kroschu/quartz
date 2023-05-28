Drakon.Tech is an IDE based on the DRAKON visual language

https://drakon.tech/ 

Створи докер контейнер для запуску Drakon.Tech в контейнері. Drakon.Tech - це IDE, що базується на візуальній мові DRAKON. Адреса проекта: https://github.com/stepan-mitkin/drakon.tech. 

Щоб створити Dockerfile для запуску Drakon.Tech в контейнері, вам потрібно налаштувати Dockerfile, який включає всі кроки встановлення, зазначені в інструкціях. Я створив приклад Dockerfile, який ви можете використовувати:

```Dockerfile
# Set base image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC
ENV RELEASE=focal
ENV DRAKON_VERSION=201811110836

# Install required packages
RUN apt-get update && \
    apt-get install -y gnupg2 curl lsb-release apt-transport-https \
    tarantool luarocks \
    lua-sec expat libexpat1-dev \
    openjdk-8-jdk tcl && \
    curl http://download.tarantool.org/tarantool/1.9/gpgkey | apt-key add - && \
    echo "deb http://download.tarantool.org/tarantool/1.9/ubuntu/ ${RELEASE} main" > /etc/apt/sources.list.d/tarantool_1_9.list && \
    echo "deb-src http://download.tarantool.org/tarantool/1.9/ubuntu/ ${RELEASE} main" >> /etc/apt/sources.list.d/tarantool_1_9.list && \
    apt-get update && \
    apt-get install -y tarantool && \
    luarocks install luautf8 && \
    luarocks install luaexpat && \
    luarocks install luasoap

# Install tarantool-http
RUN tarantoolctl rocks install http

# Install tarantool-mysql
RUN git clone https://github.com/tarantool/mysql.git tarantool-mysql && \
    cd tarantool-mysql && cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo && \
    make && make install

# Create directory structure
RUN mkdir /dewt && \
    cd /dewt && \
    mkdir app data emails feedback journal logs ssl static tmp content read && \
    echo "return {}" > app/external_creds.lua && \
    chown -R tarantool *

# Copy Drakon.Tech source code
COPY . /drakon

# Build and deploy Drakon.Tech
RUN cd /drakon && \
    ./build && \
    cp /tmp/${DRAKON_VERSION}.zip /dewt && \
    cp scripts/deploy /dewt && \
    cd /dewt && \
    ./deploy ${DRAKON_VERSION}.zip

# Copy instance configuration
COPY onprem.lua /etc/tarantool/instances.available/

# Set up instance
RUN tarantoolctl stop example && \
    rm /etc/tarantool/instances.enabled/example.lua && \
    ln -s /etc/tarantool/instances.available/onprem.lua /etc/tarantool/instances.enabled/onprem.lua

# Expose ports
EXPOSE 8090

# Start Drakon.Tech
CMD ["tarantoolctl", "start", "onprem"]
```

Зауважте, що цей Dockerfile припускає, що вихідний код Drakon.Tech знаходиться у поточному каталозі, а файл конфігурації `onprem.lua` також знаходиться у поточному каталозі. Ви повинні змінити це відповідно до вашої ситуації.

Після того, як ви створили Dockerfile, ви можете зібрати образ Docker, виконавши наступну команду:

```
docker build -t drakon_tech .
```

Тоді ви можете запустити контейнер, виконавши наступну команду:

```
docker run -d -p 8090:8090 --name drakon_tech_container drakon_tech
```

Це запустить контейнер з Drakon.Tech на порту 8090 вашої машини.