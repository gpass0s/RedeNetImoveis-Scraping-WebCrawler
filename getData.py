import urllib.request

imoveis = ['INDEX','PREÇO','ÁREA', 'LONGITUDE', 'LATITUDE', 'QTDE_QUARTOS', 'QTDE_BANHEIROS','QTDE_SUITES',
            'VAGAS_GARAGEM','PRECO','VALOR_CONDOMINIO','VALOR_IPTU', 'PAGE', 
            'CIDADE','REGIAO','BAIRRO','RUA','NUMERO']

print (','.join(imoveis))
page = 1
n = 1


while True:
    r = urllib.request.urlopen('https://www.netimoveis.com/venda/minas-gerais/belo-horizonte/apartamento/?pagina=' + str(page))
    import json
    my_data = json.loads(r.read().decode('utf-8'))
    if not my_data['lista']:
        break
    for i in range (len(my_data['lista'])):
        json= my_data['lista'][i]
        my_list = []
        my_list.append(str(n))
        my_list.append(str(json['imovel_Id']))
        my_list.append(str(json ['valorImovel']))
        my_list.append(str(json ['areaRealPrivativa']))
        my_list.append(str(json ['latitude2']))
        my_list.append(str(json ['longitude2']))
        my_list.append(str(json['quartos']))
        my_list.append(str(json['banho']))
        my_list.append(str(json['suites']))
        my_list.append(str(json ['vagaGaragem']))
        my_list.append(str(json ['valorCondominio']))
        my_list.append(str(json ['valorIptu']))
        my_list.append(str(page))
        my_list.append(str(json ['nomeCidadeAl']))
        my_list.append(str(json ['nomeRegiaoAl']))
        my_list.append(str(json ['nomeBairro']))
        my_list.append(str(json ['logradouroFake']))
        my_list.append(str(page))
        n += 1
        print (','.join(my_list))
    page += 1
    my_data.clear()
