detergente = 1.55
cerveja = 3.33
farinha = 3.93
arroz = 5.11
feijao = 4.43
valorCompra = 0
programa = 1

print('GERENCIADOR DO MERCADINHO')

while programa == 1:
    menu = int(input('Digite o código do próximo produto: 1-Detergente 2-Cerveja 3-Farinha 4-Arroz 5-Feijão 6-Finalizar compra 7-Recomeçar  '))
    if menu == 1:
        print('Detergente R$ 1,55')
        valorCompra += detergente
        print('Sub-total R$ {}'.format(valorCompra))
    if menu == 2:
        print('Cerveja R$ 3,33')
        valorCompra += cerveja
        print('Sub-total R$ {}'.format(valorCompra))
    if menu == 3:
        print('Farinha R$ 3,93')
        valorCompra += farinha
        print('Sub-total R$ {}'.format(valorCompra))
    if menu == 4:
        print('Arroz R$ 5,11')
        valorCompra += arroz
        print('Sub-total R$ {}'.format(valorCompra))
    if menu == 5:
        print('Feijão R$ 4,43')
        valorCompra += feijao
        print('Sub-total R$ {}'.format(valorCompra))
    if menu == 6:
        print('Total da compra R$ {}'.format(valorCompra))
        programa = 0
        print('Aperte 7 para recomeçar')
        menu == 7
    if menu == 7:
        programa = 0
        break