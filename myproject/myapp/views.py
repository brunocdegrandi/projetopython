from django.shortcuts import render, redirect
from .models import Produto, Cliente, FormaPagamento, Venda
from .forms import ProdutoForm, ClienteForm, FormaPagamentoForm, VendaForm

def home(request):
    return render(request, 'home.html')

# Cadastro de Produto
def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastro_produto.html', {'form': form})

# Listagem de Produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

# Edição de Produto
def edita_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'edita_produto.html', {'form': form})

# Exclusão de Produto
def exclui_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('lista_produtos')

# ... (Views para Cliente, FormaPagamento e Venda, seguindo a mesma lógica)

# Cadastro de Venda
def cadastro_venda(request):
    # ... (Lógica para criar uma nova venda, associando produto, cliente e forma de pagamento)
    return redirect('lista_vendas')

# Listagem de Vendas
def lista_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'lista_vendas.html', {'vendas': vendas})