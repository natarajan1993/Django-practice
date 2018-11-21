from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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

class PostListView(ListView): # Class Based View. Generic Django model for displaying a list
	model = Post # Just simply specify that the model we are using to display as a list model is our post model
	template_name = 'blog/home.html' # Change the default CBV naming convention
	context_object_name = 'posts' # Set what the name of the context is that the CBV needs to display. In our case it is the 'posts' context we have defined in home()
	ordering = ['-date_posted'] # Order the posts by date_posted. To reverse, use ['-date_posted']
	paginate_by = 5 # Change the number of posts per page

class UserPostListView(ListView): # CBV for posts by a user
	model = Post 
	template_name = 'blog/user_posts.html' 
	context_object_name = 'posts'
	ordering = ['-date_posted'] 
	paginate_by = 5

	def get_queryset(self): # Overwrite the default queryset function by the ListView class
		user = get_object_or_404(User, username = self.kwargs.get('username')) # Get the object or 404 of type User and then get only the attribute of username from the User model. The referenced User model already has a keyword-argument of 'username'
		return Post.objects.filter(author = user).order_by('-date_posted') # Filter all the posts objects where the author is the user and order by descending date


class PostDetailView(DetailView): # Class Based View for a detailed view of a post. What gets displayed whan a user clicks on the post
	model = Post 

class PostCreateView(LoginRequiredMixin, CreateView): # Class Based View for a detailed view of a post. What gets displayed whan a user clicks on the post
# The LoginRequiredMixin is the CBV equivalent of using the @login_required decorator. Put it as the first argument
	model = Post 
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user # Overwrite the default form_valid method to our own so we can set the author of this instance of the form to be the user in this request. We need to do this because the Post model requires we have an author
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): 
	# Use the UserPassesTestMixin to check if the user passes a certain condition. 
	model = Post 
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user # Overwrite the default form_valid method to our own so we can set the author of this instance of the form to be the user in this request. We need to do this because the Post model requires we have an author
		return super().form_valid(form)

	# Write own custom function to use our own custom tests. In this case we are making sure that the user updating the post also created the post
	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # CBV to delete a view
	model = Post
	success_url = '/' # Send them back to the homepage if the post was deleted

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False

def about(request):
    return render(request,'blog/about.html' ,{'title':'About'})

