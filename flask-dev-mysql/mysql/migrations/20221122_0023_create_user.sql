create table users(
    id varchar(255) UNIQUE,
    user_name text,
    email text not null,
    created_at DATETIME not null,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
