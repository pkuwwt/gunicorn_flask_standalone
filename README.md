
# A sample Flask app deployed by gunicorn and pyinstaller

## Usage

```
pip3 install -r requirements.txt
./compile.sh
dist/app_gunicorn/app_gunicorn --bind=127.0.0.1:8000 --workers=2
```

`127.0.0.1:8000` is the default binding address, and number of the the default workers depends on the hardware.

The directory `dist/app_gunicorn`, which is only depends on a few system libs,  can be deploy to any machine with the same (Linux) operating system distribution.

The command line options are exactly the same with `gunicorn` itself. So the help is avaiable:
```
dist/app_gunicorn/app_gunicorn -h
```

## nginx

If you want to use it with nginx, just bind it to a socket file:

```
dist/app_gunicorn/app_gunicorn --bind=unix:/tmp/gunicorn.sock
```

And then configure the `/etc/nginx/nginx.conf`:

```
location / {
	include uwsgi_params;
	uwsgi_pass unix:/tmp/gunicorn.sock;
}
```
