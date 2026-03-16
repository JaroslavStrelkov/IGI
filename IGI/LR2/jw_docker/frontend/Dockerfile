FROM node:14-bullseye-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \ python2 \ make \ g++ \ && rm -rf /var/lib/apt/lists/* \ && ln -s /usr/bin/python2 /usr/bin/python

RUN npm install -g node-gyp

COPY app/package*.json ./

RUN npm install --legacy-peer-deps

RUN npm rebuild node-sass --force

COPY app/. .

RUN npm run build:prod

FROM nginx:stable-alpine AS production

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]