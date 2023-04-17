#Simple dockerfile for creating a MySql databse banes USER_DB
#Uses the schema_creation.sql to create a table with predefined columns
#Docker build command: docker build -t local-mysqldb .
#Docker run command: docker run -dp 3306:3306 local-mysqldb

FROM mysql/mysql-server

ENV MYSQL_DATABASE=USER_DB \
    MYSQL_ROOT_PASSWORD=@uthenticateUser13 \
    MYSQL_ROOT_HOST=%

ADD schema_creation.sql /docker-entrypoint-initdb.d

EXPOSE 3306