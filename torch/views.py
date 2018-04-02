from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as django_settings
from .models import Code
# Create your views here.

@csrf_exempt
def get_file(request):
        f = request.FILES['jaf']
        if True:
            p = django_settings.BASE_DIR + '/hehe/'
            filename = p + str(f.name)
            with open(filename,'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            return HttpResponse('success')
        else:
            return HttpResponse('error')

def send_code(request):
        try:
                c = Code.objects.filter(is_read=False).order_by('id')[0]
                code = c.code
                c.is_read=True
                c.save()
                return HttpResponse(code)
        except:
                return HttpResponse('nocode')
        
