from django.shortcuts import render, redirect

people = []

class Person:
    def init(self, username, password):
        self.username = username
        self.password = password

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person
        people.append(person)
        return redirect('people')
    return render(request, 'add.html')

def show_people(request):
    context = {'people': people}
    return render(request, 'people.html', context)
