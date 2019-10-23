
pyinstaller -y \
	--hidden-import gunicorn.glogging \
	--hidden-import gunicorn.workers.sync \
	--hidden-import gunicorn.workers.ggevent \
	app_gunicorn.py

