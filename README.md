django-template-cli
===================

CLI to django template renderer

Render template contents from the command line.

Why django-template-cli
-----------------------

Ever wanted to include templated config inside your repository 
for your django app's database, webserver, crontab etc?

This management command allows you (or chef, Docker, etc) to do
so :)

Or you can use Django's `dbsync` signal to make deployment seamless.

Install
-------

Clone the repo, run `python setup.py install` to install.

Add `django_template_cli` to your `INSTALLED_APPS`.

Usage
-----

	Usage: template ([CONTEXT]) ([TEMPLATE]) 
   	Render [TEMPLATE] to stdout using [CONTEXT] 
        The context is json formatted text. 
        By default uses stdin for the template content. 
        If no stdin is supplied, assume the last argument 
        is either a path to a file or the actual content. 
        If no context is supplied, use os.environ 

See `django_template_cli.management.commands.template` for
detailed documentation.

Examples
--------

To render template from stdin using `os.environ` as context

    $> echo "{{PATH}}" | ./manage.py template
    /usr/bin:/usr/sbin:/usr/local/bin: ..etc

To render template from a file templates/main.html using 
`os.environ` as context

    $> ./manage.py template templates/main.html
    <!DOCTYPE >
    ..etc

Specify context and template

    $> ./manage.py template '{"DTYPE": "html"}' templates/main.html
    <!DOCTYPE html>
    ..etc

Specify context only

    $> echo "{{PATH}}" | ./manage.py template '{"PATH": "FOO"}'
    FOO



TODO
----

Write tests, use Django's template loaders.