FROM node:14-buster-slim

WORKDIR /app/frontend
COPY package*.json .
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]