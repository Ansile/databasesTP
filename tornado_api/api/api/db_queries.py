from start import db

user_select_by_id = db.prepare('SELECT * FROM "user" WHERE id = $1::BIGINT')
user_select_by_nickname = db.prepare('SELECT * FROM "user" WHERE nickname = $1::CITEXT')

forum_select_by_id = db.prepare('SELECT * FROM forum WHERE id = $1::BIGINT')

thread_select_by_id = db.prepare('SELECT * FROM thread WHERE id = $1::BIGINT')
thread_select_by_slug = db.prepare('SELECT * FROM thread WHERE slug = $1::CITEXT')

