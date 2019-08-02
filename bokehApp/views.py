from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse


# Create your views here.



def graph(request):
    # blogs = Blog.objects
    # return render(request, 'blog/allblogs.html', {'blogs':blogs})
    first_graph = 'my first bokeh graph'
    return HttpResponse(first_graph)