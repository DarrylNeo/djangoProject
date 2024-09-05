from django.shortcuts import render

def image_detection_view(request):
    return render(request, 'image_detection/live_feed.html')


