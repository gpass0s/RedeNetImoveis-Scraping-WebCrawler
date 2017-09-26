import urllib.request

imoveis = ['INDEX','PREÇO','QTDE_QUARTOS','QTDE_BANHEIROS','QTDE_SUITES',
            'AREA','VAGAS_GARAGEM','PREÇO','VALOR_CONDOMINIO','VALOR_IPTU','CIDADE',
            'REGIAO','BAIRRO','RUA']

print (','.join(imoveis))
page = 1
n = 1


while True:
    r = urllib.request.urlopen('https://www.netimoveis.com/venda/minas-gerais/belo-horizonte/apartamento/?pagina=' + str(page))
    import json
    my_data = json.loads(r.read())
    if not my_data['lista']:
        break
    page += 1
    for i in range (len(my_data['lista'])):
        json= my_data['lista'][i]
        my_list = []
        my_list.append(str(n))
        my_list.append(str(json['quartos']))
        my_list.append(str(json['banho']))
        my_list.append(str(json['suites']))
        my_list.append(str(json ['areaRealPrivativa']))
        my_list.append(str(json ['vagaGaragem']))
        my_list.append(str(json ['valorImovel']))
        my_list.append(str(json ['valorCondominio']))
        my_list.append(str(json ['valorIptu']))
        my_list.append(str(json ['nomeCidadeAl']))
        my_list.append(str(json ['nomeRegiaoAl']))
        my_list.append(str(json ['nomeBairro']))
        my_list.append(str(json ['logradouroFake']))
        n += 1
        print (','.join(my_list))
    my_data.clear()
