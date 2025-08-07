from .models import Registration
def user_with_scores(request):
    print(">>> CONTEXT PROCESSOR RUNNING")  # Debug line
    task = None
    if request.session.get('email'):
        try:
            task = Registration.objects.get(email=request.session['email'])
        except Registration.DoesNotExist:
            task = None
    return {'task': task}
