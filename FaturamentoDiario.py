import json

faturamentoJson = '''
{
    "faturamento": [1000, 2000, 0, 3000, 0, 1500, 0, 2700, 3500, 0, 0, 3200, 1000, 2800, 0, 0, 5000, 4500, 4000, 0, 0, 1800, 0, 0, 0, 2100, 1500, 0, 0, 1000]
}
'''

dados = json.loads(faturamentoJson)
faturamento = dados["faturamento"]

faturamentoValidos = [f for f in faturamento if f > 0]

menorFaturamento = min(faturamentoValidos)
maiorFaturamento = max(faturamentoValidos)

mediaFaturamento = sum(faturamentoValidos) / len(faturamentoValidos)

diasAcimaDaMedia = len([f for f in faturamentoValidos if f > mediaFaturamento])

print(f"Menor valor de faturamento: R$ {menorFaturamento}")
print(f"Maior valor de faturamento: R$ {maiorFaturamento}")
print(f"Dias com faturamento acima da média: {diasAcimaDaMedia}")
