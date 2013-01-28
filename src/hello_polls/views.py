from django.template import Context
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from hello_polls.models import MyPoll
from hello_polls.models import MyChoice
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    latest_poll_list = MyPoll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('hello_polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))


def detail(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    return render_to_response('hello_polls/detail.html', {'poll': p},
                               context_instance=RequestContext(request))

# ...
def vote(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    try:
        selected_choice = p.mychoice_set.get(pk=request.POST['choice'])
    except (KeyError, MyChoice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('hello_polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hello_polls.views.results', args=(p.id,)))
    
def results(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    return render_to_response('hello_polls/results.html', {'poll': p})    
