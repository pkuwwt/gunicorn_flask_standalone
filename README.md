
# A sample Flask app deployed by gunicorn and pyinstaller

PyInstaller is great to bundle a python application as a single standalone executable, so that it is more convienent to deploy and to dysfunction the source code.

But what about flask application? Flask applications are often distributed as modules, which rely on other production web servers like `uwsgi`.

Fortunately, there is a python implementation of uwsgi: `gunicorn`. And this project uses gunicorn to wrap flask as a standalone application, which is then bundled by PyInstaller.

## Usage

```
pip3 install -r requirements.txt
./compile.sh
dist/app_gunicorn/app_gunicorn --bind=127.0.0.1:8000 --workers=2
```

`127.0.0.1:8000` is the default binding address, and the default number of workers depends on the hardware (`2 * NUM_CPU + 1`).

The directory `dist/app_gunicorn`, which is only depends on a few system libs,  can be deployed to any machine with the same (Linux) operating system distribution.

The command line options are exactly the same with `gunicorn` itself. So the help is available:
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
