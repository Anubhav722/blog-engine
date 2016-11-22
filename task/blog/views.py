from django.shortcuts import render, get_object_or_404
from blog.models import Content, Content_Types

# Create your views here.
def index(request):
    queryset=Content.objects.all()
    context={
        "text":"Posts",
        "objects":queryset,
    }
    
    return render(request, "index.html", context)
    
    
def detail(request, id):
    instance =get_object_or_404(Content, id=id)
    
    #content=get_object_or_404(Contents_Type, id=id)
    object_list=instance.content_types_set.all()
    context={
        "title":instance.title,
        "instance":instance,
        
        "object_list":object_list,
        
        
    }
    return render(request, "detail.html", context)