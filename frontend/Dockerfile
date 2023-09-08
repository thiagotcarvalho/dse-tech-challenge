FROM node:14-slim
WORKDIR /app/frontend
COPY package*.json .
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]