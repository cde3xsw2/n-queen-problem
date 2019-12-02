# N-queen problem

Solves the n-queen problem.

## Database instalation 
```bash
sudo apt-get install postgresql postgresql-contrib
psql -h localhost -p 54320 -U postgres
postgres# create database nqueen;
```

## Docker-compose Installation 

Start docker-compose.

```bash
sudo docker build -t n-queen-problem .
sudo docker-compose build
sudo docker-compose up -d --remove-orphans
```
		
## Usage

```bash
		sudo docker-compose run solve python /code/solve.py save-in-db 8
		sudo docker-compose run solve python /code/solve.py list-results 8
		
		Options:
			calculate num-of-queens(i.e. calculate 8)
			save-in-db num-of-queens (i.e. save-in-db 8)
			list-results num-of-queens (i.e. list-results 8)
			find-first num-of-queens (i.e.find-first 8)
```