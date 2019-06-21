from django.shortcuts import render
from .forms import formMpi

def formpi(request):
    if request.method == 'POST':
        form=formMpi(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid(): #pregunto si mis datos son validos
            form.save() #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=formMpi()#caso contrario atualizo la misma pagina del forulario
    return render(request,"mpi/imagens.html",{'form':form})