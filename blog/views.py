from django.shortcuts import render

# Create your views here.
def post_list(reques):
	return render(reques, 'blog/post_list.html', {})
