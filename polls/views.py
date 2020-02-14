from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
import  datetime


from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import datetime,timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save


from .models import Choice, Question,Voter

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'




    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

#




class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request, question_id):
    if Voter.objects.filter(question_id=question_id, user_id=request.user.id).exists():
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "Sorry, but you have already voted."
            })

    else:
            question = get_object_or_404(Question, pk=question_id)
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
            except (KeyError, Choice.DoesNotExist):

                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
            else:
                    selected_choice.votes += 1
                    selected_choice.save()
                    Voter.objects.create(question_id=question_id, user_id=request.user.id)

                    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

