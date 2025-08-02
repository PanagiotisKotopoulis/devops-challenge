# Use official nginx base image
FROM nginx:alpine

# Remove default Nginx HTML files
RUN rm -rf /usr/share/nginx/html/*

# Copy our index.html into Nginx's serving directory
COPY index.html /usr/share/nginx/html

# Expose port 80 for web traffic
EXPOSE 80
