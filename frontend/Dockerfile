FROM node:14 as build
WORKDIR /app
COPY package.json .
RUN npm i --production --silent

COPY . .
RUN npm run build:docker --silent

FROM nginx:stable-alpine as serving
EXPOSE 80

COPY --from=build /app/build /usr/share/nginx/html
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]