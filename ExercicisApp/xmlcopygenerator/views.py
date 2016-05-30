from django.core.urlresolvers import reverse
from django.http import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
from django.contrib.auth.decorators import user_passes_test
import datetime
import sys

# Create your views here.
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def xmlcopygenerator(request):
    sysout = sys.stdout
    Fitxer = "xmlcopygenerator/BDDBackup/" + str(datetime.datetime.now()).replace(" ","").replace(":","-")+".xml"
    sys.stdout = open (Fitxer, 'w')
    call_command('dumpdata',indent=2,format='xml')
    sys.stdout = sysout
    messages.success(request, 'Backup creat correctament.')
    return HttpResponseRedirect(reverse('exercicisapp:repartir'))
