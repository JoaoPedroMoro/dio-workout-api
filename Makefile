venv:
	@.\.workoutapi\Scripts\activate

run:
	@uvicorn workout_api.main:app --reload

docker_up:
	@docker-compose up -d

docker_down:
	@docker-compose down

create-migrations:
	@set PYTHONPATH=%PYTHONPATH%;%cd% && alembic revision --autogenerate -m $(d)

run-migrations:
	@set PYTHONPATH=%PYTHONPATH%;%cd% &&  alembic upgrade head