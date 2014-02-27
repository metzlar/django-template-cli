from django.core.management.base import BaseCommand, CommandError
from django.template import Context, Template

import os
import json
import sys
import select


class Command(BaseCommand):
    help = (
        'Usage: template ([CONTEXT]) ([TEMPLATE]) '
        'Render [TEMPLATE] to stdout using [CONTEXT] '
        'The context is json formatted text. '
        'By default uses stdin for the template content. '
        'If no stdin is supplied, assume the last argument '
        'is either a path to a file or the actual content. '
        'If no context is supplied, use os.environ '
    )

    def handle(self, *args, **options):

        template = None
        context = None
        
        # if stdin contains anything it is the template_content
        r, w, x = select.select([sys.stdin], [], [], 0)
        if r:
            template = Template(''.join(t.read() for t in r))
        else:
            # one of the arguments must be the path to the template
            if len(args) == 1:
                template = args[0]
                # in this case the context must be os.environ
                context = Context(os.environ)
            elif len(args) == 2:
                template = args[1]
                # in this case the context must be the first arg
                # see below
            else:
                raise CommandError((
                    'Either supply template content through stdin, '
                    'as argument or the path to a file as argument'
                ))
            if os.path.exists(template):
                with open(template) as f:
                    template = Template(f.read())
            else:
                template = Template(template)

        if context is None and len(args) > 0:
            if os.path.exists(args[0]):
                # load the file
                context = Context(json.load(args[0]))
            else:
                # load the argument value
                context = Context(json.loads(args[0]))
        else:
            context = Context(os.environ)
            
        self.stdout.write(template.render(context))