from django.shortcuts import render
from datetime import datetime
from .models import Post

#posts = [
#    {
#        'author' : 'Nate',
#        'title' : 'Post 1',
#        'content' : 'First post content',
#        'date_posted' : datetime.now()
#    },
#    {
#        'author' : 'Test User',
#        'title' : 'Post 2',
#        'content' : 'Second post content',
#        'date_posted' : datetime.now()
#    },
#]

def home(request):
    context = {'posts':Post.objects.all()} # Instead of defining our own data, use the Post tables we saved in the db
    return render(request,'blog/home.html', context) # Render first argument is the request, second is the template to be rendered and third is the external information referred to inside the template
def about(request):
    return render(request,'blog/about.html' ,{'title':'About'})

