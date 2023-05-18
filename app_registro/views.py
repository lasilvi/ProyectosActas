from django.shortcuts import render
from .forms import RegisterForm, RegisterFormUser,RegisterFormDevelopment,DevelopmentFormSet,ResponsibleDevelopmentFormSet,RegisterFormCommitment
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
        #    send_mail(
        #        'Nuevo mensaje de contacto',
        #        f'Nombre: {name}\nEmail: {email}\nMensaje: {message}',
        #        email,
        #        ['tu@email.com'],
        #        fail_silently=False,
        #    )
            return render(request, 'success.html')
    else:
        form = RegisterForm()
        #formuser = RegisterFormUser()
    return render(request, 'app_registro/formulario.html', {'form': form })

def RegisterUser(request):
    if request.method == 'POST':
        formuser = RegisterFormUser(request.POST)
        if formuser.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
        #    send_mail(
        #        'Nuevo mensaje de contacto',
        #        f'Nombre: {name}\nEmail: {email}\nMensaje: {message}',
        #        email,
        #        ['tu@email.com'],
        #        fail_silently=False,
        #    )
            return render(request, 'success.html')
    else:
        formuser = RegisterFormUser()
    return render(request, 'app_registro/formulario2.html', {'form': formuser })

def RegisterDevelopment(request):
    development_formset = DevelopmentFormSet(request.POST or None, prefix='development')
    Responsible_formset = ResponsibleDevelopmentFormSet(request.POST or None, prefix='commitment')

    if request.method == 'POST':
        #formdevelop = RegisterFormDevelopment(request.POST)
        if development_formset.is_valid() and Responsible_formset.is_valid():
            #development_formset.save()
            #Responsible_formset.save()
            return render(request, 'success.html')
    context = {
        'development_formset': development_formset,
        'Responsible_formset': Responsible_formset,
    }
    return render(request, 'app_registro/formulario3.html',  context )

def RegisterCommintment(request):
    if request.method == 'POST':
        form = RegisterFormCommitment(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
        #    send_mail(
        #        'Nuevo mensaje de contacto',
        #        f'Nombre: {name}\nEmail: {email}\nMensaje: {message}',
        #        email,
        #        ['tu@email.com'],
        #        fail_silently=False,
        #    )
            return render(request, 'success.html')
    else:
        form = RegisterFormCommitment()
        #formuser = RegisterFormUser()
    return render(request, 'app_registro/formulario4.html', {'form': form })
