
## Dockerfile 

``` Dockerfile


FROM arm64v8/node:14-alpine

# Set the working directory

WORKDIR /app

# Copy package.json and package-lock.json to the working directory

COPY package*.json ./

# Install app dependencies

RUN npm install

# Copy the rest of the application files to the working directory

COPY . .

# Build the application

RUN npm run build

# Set the environment variable

ENV NODE_ENV=production

Expose port 3000

EXPOSE 3000

# Start the application

CMD ["npm", "start"]

```


Збережіть цей файл як Dockerfile у кореневому каталозі проекту.
Щоб зібрати і запустити контейнер, перейдіть до кореневого каталогу проекту і виконайте наступну команду:
`docker build -t kroschu/langchain-ui-arm65v8 .`

`docker run -p 3000:3000 kroschu/langchain-ui-arm65v8`


Це призведе до створення образу і запуску контейнера на порту 3000. Відкрийте веб-браузер і перейдіть за адресою http://localhost:3000, щоб переглянути додаток.
