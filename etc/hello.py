upstream example_mysite {

  server 0.0.0.0:8080 fail_timeout=0;
}
server {
  listen 80;
  client_max_body_size 4G;
  server_name example.com www.example.com;

  keepalive_timeout 5;

  # path for static files
  root /home/box/web;

  location / {
      # checks for static file, if not found proxy to app
      try_files $uri @proxy_to_app;
  }
  location /hello/ {
      alias /home/box/web;     
  }

  location @proxy_to_app {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host;
      proxy_redirect off;
      proxy_pass http://gunicorn_mysite;
  }

}
