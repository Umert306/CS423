# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy application files
COPY . .

# Build the React app
RUN npm run build

# Expose port
EXPOSE 80

# Use an nginx server to serve the app
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
