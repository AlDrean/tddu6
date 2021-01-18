# tddu6

Este trabalho de MC646 busca exercitar o modelo TDD de criação de testes para um programa com a seguinte funcionalidade:

Uma feature comum em diferentes aplicações que utilizam arquivos como armazenamento (editores de texto, planilhas, editores gráficos, ...) é a Lista de Arquivos Recentes, que permite abrir mais rapidamente um arquivo recém utilizado.

Alguns exemplos de comportamentos são:

Quando o programa está executando pela primeira vez, essa lista está vazia;
Quando um arquivo é aberto, ele é adicionado à lista de arquivos recentes;
Se um arquivo aberto já está na lista, este é levado ao topo da lista, sem conter itens duplicados na lista
Se a lista alcança seu limite (normalmente de 10 a 15 itens na lista), o item mais antigo é removido quando um novo item é adicionado.
A lista pode ser esvaziada a qualquer momento
A atualização da lista pode ser desabilitada/habilitada. Caso seja desabilitada, os arquivos já existentes ficarão na lista, mas não serão adicionados novos arquivos.
