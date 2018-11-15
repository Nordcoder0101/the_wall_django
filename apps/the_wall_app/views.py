from django.shortcuts import render, redirect
from .models import Message, Comment
from apps.login_and_registration.models import User

def index(request):
    random_word = request.GET.get('random_word')
    print(f"{random_word}********") 
    if random_word != request.session['random_word']:
        return redirect('/')
        

    context = {
      'current_user': User.objects.get(id = request.session['logged_in_user_id']),
      'all_messages': Message.objects.all(),
      'all_comments': Comment.objects.all()
    }
    return render(request, 'the_wall_app/the_wall.html', context)

def create_message(request):
    if request.method == "POST":
        message_to_post = request.POST['message_text']
        posting_user = User.objects.get(id=request.session['logged_in_user_id'])
        new_message = Message.objects.create(created_by = posting_user, content = message_to_post)
        print(new_message)
        return redirect("/wall?random_word={}".format(request.session['random_word']))
    
def create_comment(request):
    if request.method == "POST":
        comment_to_post = request.POST['comment_text']
        message_to_post_on = Message.objects.get(id=request.POST['message_id'])
        posting_user = User.objects.get(id=request.session['logged_in_user_id'])
        new_comment = Comment.objects.create(created_by=posting_user, posted_on = message_to_post_on, content=comment_to_post)
        print(new_comment.__dict__)
        return redirect("/wall?random_word={}".format(request.session['random_word']))

def logout(request):
    request.session.clear()
    return redirect('/')
