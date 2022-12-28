ifneq (,$(wildcard ./.env))
include .env
export 
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

down:
	docker compose down

show-logs:
	docker compose logs

down-v:
	docker compose down -v

volume:
	docker volume inspect instagram-influencer_postgres_data

instagram-influencer-db:
	docker compose exec postgres-db psql --username=kene --dbname=instagram-influencer
