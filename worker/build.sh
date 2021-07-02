# worker first
docker build -t glitch-worker .
docker run --rm -it -p 7607:7607 --name glitch-worker glitch-worker

