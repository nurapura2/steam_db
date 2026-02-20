CREATE TABLE "users" (
  "user_id" integer PRIMARY KEY,
  "username" varchar,
  "email" varchar,
  "password" varchar,
  "created_at" date
);

CREATE TABLE "wallets" (
  "wallet_id" integer PRIMARY KEY,
  "user_id" integer,
  "currency" varchar,
  "balance" numeric,
  "updated_at" date
);

CREATE TABLE "games" (
  "game_id" integer PRIMARY KEY,
  "title" varchar,
  "price" numeric,
  "release_date" date,
  "age_rating" varchar,
  "description" varchar
);

CREATE TABLE "system_requirements" (
  "requirement_id" integer PRIMARY KEY,
  "game_id" integer,
  "platform" varchar,
  "requirement_type" varchar,
  "cpu" varchar,
  "gpu" varchar,
  "ram_gb" integer,
  "storage_gb" integer
);

CREATE TABLE "library" (
  "game_id" integer,
  "user_id" integer,
  "purchase_id" integer,
  "added_date" date,
  PRIMARY KEY ("user_id", "game_id")
);

CREATE TABLE "purchases" (
  "purchase_id" integer PRIMARY KEY,
  "user_id" integer,
  "purchase_type" varchar,
  "payment_method" varchar,
  "status" varchar,
  "purchase_date" date
);

CREATE TABLE "purchases_item" (
  "purchase_item_id" integer PRIMARY KEY,
  "game_id" integer,
  "purchase_id" integer,
  "price_at_purchase" integer
);

CREATE TABLE "reviews" (
  "review_id" integer PRIMARY KEY,
  "user_id" integer,
  "game_id" integer,
  "review_type" varchar,
  "comment" varchar,
  "review_date" date
);

ALTER TABLE "wallets" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "library" ("user_id");

ALTER TABLE "purchases" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "purchases_item" ADD FOREIGN KEY ("purchase_id") REFERENCES "purchases" ("purchase_id");

ALTER TABLE "library" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "system_requirements" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "purchases_item" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("game_id");

ALTER TABLE "purchases" ADD FOREIGN KEY ("purchase_id") REFERENCES "library" ("purchase_id");
