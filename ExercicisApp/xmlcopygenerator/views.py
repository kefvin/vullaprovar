from django.core.urlresolvers import reverse
from django.http import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
import datetime
import sys

# Create your views here.
@login_required
def xmlcopygenerator(request):
    sysout = sys.stdout
    Fitxer = "/media/BDDBackup" + str(datetime.datetime.now()).replace(" ","").replace(":","-")+".xml"
    sys.stdout = open (Fitxer, 'w')
    call_command('dumpdata',indent=2,format='xml')
    sys.stdout = sysout
    messages.success(request, 'Backup creat correctament.')
    return HttpResponseRedirect(reverse('exercicisapp:repartir'))
