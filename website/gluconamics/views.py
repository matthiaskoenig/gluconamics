from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('gluconamics/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

    # return HttpResponse("Hello, world. You are visiting gluconamics.")

def newsletter(request):
    print request.POST

    try:
        email = request.POST['email']
    except KeyError:
        # Redisplay the homepage
        return render(request, 'index.html', {
            'error_message': "You didn't select a choice.",
        })
    else:
        pass

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

