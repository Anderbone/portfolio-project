from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Blog
import markdown
# Create your views here.



def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk = blog_id)

    detailblog.body = markdown.markdown(detailblog.body,
        extenions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ]

    )
    return render(request, 'blog/detail.html', {'blog':detailblog})
