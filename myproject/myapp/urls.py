from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.cadastro_produto, name='cadastro_produto'),
    path('produtos/<int:produto_id>/editar/', views.edita_produto, name='edita_produto'),
    path('produtos/<int:produto_id>/excluir/', views.exclui_produto, name='exclui_produto'),

    # URLs para clientes, formas de pagamento e vendas
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    # ... (outras URLs para clientes)
    path('formas-pagamento/', views.lista_formas_pagamento, name='lista_formas_pagamento'),
    # ... (outras URLs para formas de pagamento)
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/nova/', views.cadastro_venda, name='cadastro_venda'),
]