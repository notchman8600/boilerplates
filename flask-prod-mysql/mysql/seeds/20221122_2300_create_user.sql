-- テスト用ユーザーデータ
insert into
    users(
        id,
        user_name,
        email,
        created_at
    )
values
    (
        "example-user-id-1",
        "hoge",
        "hoge@example.com",
        CURRENT_TIMESTAMP
    );