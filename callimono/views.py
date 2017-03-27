from django.shortcuts import render

def post_list(request):
    return render(request, 'callimono/post_list.html', {})
