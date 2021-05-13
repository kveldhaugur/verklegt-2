from .models import SessionHistory


def his(request):
    if request.session.session_key != None:
        context = {
            "history": [x.HistoryStr for x in SessionHistory.objects.filter(SessionID=request.session.session_key)]
        }
    else:
        context = {
            "history": None
        }

    return context