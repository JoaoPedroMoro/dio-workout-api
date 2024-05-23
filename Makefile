venv:
	@.\.workoutapi\Scripts\activate

run:
	@uvicorn workout_api.main:app --reload

docker-up:
	@docker-compose up -d

docker-down:
	@docker-compose down

create-migrations:
	@set PYTHONPATH=%PYTHONPATH%;%cd% && alembic revision --autogenerate -m $(d)

run-migrations:
	@set PYTHONPATH=%PYTHONPATH%;%cd% &&  alembic upgrade head