CREATE TABLE "users" (
  "user_id" serial PRIMARY KEY,
  "username" text UNIQUE NOT NULL,
  "email" text UNIQUE NOT NULL,
  "password_hash" text NOT NULL,
  "created_at" timestamptz DEFAULT (now())
);

CREATE TABLE "wallets" (
  "wallet_id" serial PRIMARY KEY,
  "user_id" integer UNIQUE NOT NULL,
  "currency" varchar(3) DEFAULT 'USD',
  "balance" numeric(12,2) DEFAULT 0,
  "updated_at" timestamptz DEFAULT (now())
);

CREATE TABLE "games" (
  "game_id" serial PRIMARY KEY,
  "developer_id" integer,
  "title" text NOT NULL,
  "price" numeric(12,2) NOT NULL DEFAULT 0,
  "release_date" timestamptz,
  "age_rating" text,
  "description" text
);

CREATE TABLE "sessions" (
  "session_id" serial PRIMARY KEY,
  "user_id" integer NOT NULL,
  "game_id" integer NOT NULL,
  "start_time" timestamptz DEFAULT (now()),
  "end_time" timestamptz
);

CREATE TABLE "promotions" (
  "promo_id" serial PRIMARY KEY,
  "code" varchar(20) UNIQUE NOT NULL,
  "discount_percent" numeric(5,2),
  "start_date" timestamptz,
  "end_date" timestamptz
);

CREATE TABLE "reports" (
  "report_id" serial PRIMARY KEY,
  "top_game_id" integer,
  "total_revenue" numeric(15,2),
  "average_rating" numeric(3,2),
  "generated_at" timestamptz DEFAULT (now())
);

CREATE TABLE "badges" (
  "badge_id" serial PRIMARY KEY,
  "user_id" integer NOT NULL,
  "title" text NOT NULL,
  "awarded_at" timestamptz DEFAULT (now())
);

CREATE TABLE "library" (
  "game_id" integer,
  "user_id" integer,
  "purchase_id" integer,
  "added_date" timestamptz DEFAULT (now()),
  PRIMARY KEY ("user_id", "game_id")
);

CREATE TABLE "purchases" (
  "purchase_id" serial PRIMARY KEY,
  "user_id" integer NOT NULL,
  "purchase_type" text,
  "payment_method" text,
  "status" text,
  "purchase_date" timestamptz DEFAULT (now()),
  "promo_id" integer
);

CREATE TABLE "purchases_item" (
  "purchase_item_id" serial PRIMARY KEY,
  "game_id" integer,
  "purchase_id" integer,
  "price_at_purchase" numeric(12,2) NOT NULL
);

CREATE TABLE "reviews" (
  "review_id" serial PRIMARY KEY,
  "user_id" integer,
  "game_id" integer,
  "review_type" text,
  "comment" text,
  "review_date" timestamptz DEFAULT (now())
);

CREATE TABLE "developers" (
  "developer_id" serial PRIMARY KEY,
  "name" text NOT NULL,
  "country" text
);

CREATE TABLE "categories" (
  "category_id" serial PRIMARY KEY,
  "name" text UNIQUE NOT NULL
);

CREATE TABLE "game_categories" (
  "game_id" integer,
  "category_id" integer,
  PRIMARY KEY ("game_id", "category_id")
);

CREATE TABLE "friends" (
  "user_id" integer,
  "friend_id" integer,
  "status" text,
  PRIMARY KEY ("user_id", "friend_id")
);

CREATE TABLE "messages" (
  "message_id" serial PRIMARY KEY,
  "sender_id" integer,
  "receiver_id" integer,
  "content" text NOT NULL,
  "sent_at" timestamptz DEFAULT (now()),
  "is_read" boolean DEFAULT false
);

CREATE TABLE "achievements" (
  "achievement_id" serial PRIMARY KEY,
  "game_id" integer,
  "title" text NOT NULL,
  "description" text
);

CREATE TABLE "user_achievements" (
  "user_id" integer,
  "achievement_id" integer,
  "unlocked_at" timestamptz DEFAULT (now()),
  PRIMARY KEY ("user_id", "achievement_id")
);

COMMENT ON COLUMN "promotions"."discount_percent" IS 'e.g. 15.00 for 15%';

ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "wallets" ("user_id");

ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "library" ("user_id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "user_achievements" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "badges" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "friends" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "friends" ADD FOREIGN KEY ("friend_id") REFERENCES "users" ("user_id");

ALTER TABLE "messages" ADD FOREIGN KEY ("sender_id") REFERENCES "users" ("user_id");

ALTER TABLE "messages" ADD FOREIGN KEY ("receiver_id") REFERENCES "users" ("user_id");

ALTER TABLE "games" ADD FOREIGN KEY ("developer_id") REFERENCES "developers" ("developer_id");

ALTER TABLE "game_categories" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "game_categories" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("category_id");

ALTER TABLE "library" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "sessions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "sessions" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "reports" ADD FOREIGN KEY ("top_game_id") REFERENCES "games" ("game_id");

ALTER TABLE "purchases" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "purchases_item" ADD FOREIGN KEY ("purchase_id") REFERENCES "purchases" ("purchase_id");

ALTER TABLE "purchases_item" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "purchases" ADD FOREIGN KEY ("purchase_id") REFERENCES "library" ("purchase_id");

ALTER TABLE "purchases" ADD FOREIGN KEY ("promo_id") REFERENCES "promotions" ("promo_id");

ALTER TABLE "achievements" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "user_achievements" ADD FOREIGN KEY ("achievement_id") REFERENCES "achievements" ("achievement_id");
