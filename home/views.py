from django.shortcuts import render, HttpResponse
from home.models import Contact, Files
import os
from portfolio import settings
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name,email,message)
        form = Contact(name=name, email=email, message=message)
        form.save()

    context = {
        'file': Files.objects.all()
    }

    return render(request, 'home.html', context)



def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    
    raise Http404