from django.shortcuts import render
from .models import Consumer


# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def list_view(request):
    list_consumers = Consumer.objects.all()
    count_consumers = Consumer.objects.count()

    context = {
        'list_consumers': list_consumers,
        'count_consumers': count_consumers,
    }

    return render(request, 'calculator/list.html', context=context)
    # Create the first view here.


# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the second view here.
    pass
