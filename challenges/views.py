from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

monthly_challenges = {
    'january': "Try a 30-day plank challenge in January.",
    'February': "Participate in a random act of kindness every day in February.",
    'March': "Take a daily photo walk in March and share your favorite shots.",
    'April': "Try a new recipe every week in April.",
    'May': "Practice mindfulness meditation for 15 minutes every day in May.",
    'June': "Learn a new word every day in June and use it in a sentence.",
    'July': "Try a new physical activity every week in July.",
    'August': "Read a new book every week in August.",
    'September': "Try a new hobby every week in September.",
    'October': "Challenge yourself to waste less food in October.",
    'November': "Practice gratitude by writing down three things you're thankful for every day in November.",
    'December': "Challenge yourself to spread holiday cheer to someone new every day in December."
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        raise Http404()
    else:
        return HttpResponseRedirect(reverse('month', args=[months[month - 1]]))


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'challenge': {
                'title': month.capitalize() + '\'s challenge',
                'text': challenge_text
            },
        })
    except:
        raise Http404()


def unknown_month_error(request):
    pass
#     return HttpResponseNotFound(render_to_string('page-not-found.html'))
