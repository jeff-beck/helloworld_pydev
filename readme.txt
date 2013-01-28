
database API commands executed in the shell

from hello_polls.models import MyPoll, MyChoice
from django.utils import timezone

objects.all
MyPoll.objects.all()

objects.get
MyPoll.objects.get(id=1)


objects.filter
MyPoll.objects.filter(id=1)



# object creation
p = MyPoll(question="What's you favorite color?", pub_date=timezone.now())
p.save()

# field update and save
p = MyPoll.objects.get(pk=2)
>>> p.question = "Who is your favorite person?"
>>> p.save()
    
# set filter
MyChoice.objects.filter(poll__pub_date__year=current_year)

# delete
c = p.mychoice_set.filter(choice__startswith='Just hacking')
c.delete()