from django.shortcuts import render



def index(request):
    return render(request,'myapp/index.html')

def contact(request):
    return render(request,'myapp/contact.html')



def topics_detail(request):
    return render(request,'myapp/topics-detail.html')

def topics_listing(request):
    return render(request,'myapp/topics-listing.html')
