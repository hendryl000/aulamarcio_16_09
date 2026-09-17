from django.shortcuts import redirect, render

from .forms import LivroForm
from .models import Livro


def lista_livros(request):
    livros = Livro.objects.all()
    
    nome = request.GET.get("nome", "").strip()
    tipo = request.GET.get("tipo", "").strip()
    categoria = request.GET.get("categoria", "").strip()
    
    if nome:
        livros = livros.filter(titulo__icontains=nome)

    if tipo:
        livros = livros.filter(tipo_acervo=tipo)

    if categoria:
        livros = livros.filter(categoria=categoria)
        
    contexto = {
        "livros": livros,
        "tipos_acervo": Livro.TIPO_ACERVO_CHOICES,
        "categorias": Livro.CATEGORIA_CHOICES,
        "filtros": {
            "nome": nome,
            "tipo": tipo,
            "categoria": categoria,
        },
    }
    
    return render(request, "acervo/lista.html", {"livros": livros})


def novo_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = LivroForm()

    return render(request, "acervo/form.html", {"form": form})
