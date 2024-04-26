from django.shortcuts import render
from django.http import JsonResponse
from .models import Carro, Venda

# View para listar carros disponíveis
def listar_carros(request):
    # Consulta todos os carros do banco de dados
    carros = Carro.objects.all()
    # Converte os objetos Carro em uma lista de dicionários
    carros_list = [{'marca': carro.marca, 'modelo': carro.modelo, 'ano': carro.ano, 'preco': carro.preco} for carro in carros]
    # Retorna a lista de carros em formato JSON
    return JsonResponse(carros_list, safe=False)

# View para registrar uma venda
def registrar_venda(request):
    if request.method == 'POST':
        data = request.POST
        carro_id = data.get('carro_id')
        cliente_nome = data.get('cliente_nome')
        # Obtém o objeto Carro correspondente ao ID fornecido
        carro = Carro.objects.get(pk=carro_id)
        # Calcula o valor da venda com um adicional de 10% de lucro
        valor_venda = carro.preco * 1.1  
        # Cria um novo registro de venda no banco de dados
        Venda.objects.create(carro=carro, cliente_nome=cliente_nome, valor_venda=valor_venda)
        # Retorna uma resposta de sucesso em formato JSON
        return JsonResponse({'message': 'Venda registrada com sucesso'})
    else:
        # Retorna um erro de método não permitido se a requisição não for do tipo POST
        return JsonResponse({'error': 'Método não permitido'}, status=405)
