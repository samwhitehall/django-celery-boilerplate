import datetime

from django.http import HttpResponse

from fancy.tasks import expensive_task


def expensive_view(request, word):
    now = datetime.datetime.now().isoformat()
    result = expensive_task.delay(word).get()

    html = '''
        <body>
            <strong>{now}</strong>: {word} -> <em>{result}</em>
        </body>
    '''

    response = html.format(**locals())
    return HttpResponse(response)
