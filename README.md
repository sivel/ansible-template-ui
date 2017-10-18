# ansible-template-ui
Web UI for testing ansible templates

## Docker Container

```
docker build -t ansible-template-ui docker/devel
```

## Running

### Dev

```
python server.py
```

### Production

```
pip install gevent gunicorn
gunicorn -k gevent server:app
```
