from django.shortcuts import render, redirect
from .models import Ticket

def deadlines(request):
    if request.method == 'POST':
        #print (request.POST)
        #deadline = request.POST['deadline']
        for elem in request.POST.keys():
        	if elem.isdigit():
        		ticket = Ticket.objects.filter(id=int(elem))[0]
        		ticket.finished = True
        		ticket.save()

        #ticket = Ticket(title=title, text=text, deadline=deadline, finished=False)
        #ticket.save()

        return redirect('/')
    else:
        tickets_ = Ticket.objects.order_by('deadline').filter(finished=False)
        return render(request, 'timet/deadlines.html', {'tickets':tickets_})

def achieved(request):
    tickets_ = Ticket.objects.order_by('deadline').filter(finished=True)
    return render(request, 'timet/achieved.html', {'tickets':tickets_})


def newTicketForm(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        deadline = request.POST['deadline']

        ticket = Ticket(title=title, text=text, deadline=deadline, finished=False)
        ticket.save()

        return redirect('/')
    else:
        return render(request, 'timet/new_ticket.html')

