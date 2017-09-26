# Rede-NetImoveis-Web-Crawler-
Neste repositório encontra-se um simples script que escrevi para extrair algumas informações dos anúncios do site da Rede Net Imoveis a fim de obter um dataSet para o meu trabalho de conclusão de curso. Se você trabalha para essa empresa, por favor não fique zangado hahaha. Meu único objetivo é obter alguns dados para eu poder brincar de ML e Data Science... :) 

Por ser belo horizontino de coração, o código escrito extrai informações da cidade de Belo Horizonte, mas isso pode ser facilmente alterado. Basta alterar o link do json na linha 7 do código. No meu caso esse link é: https://www.netimoveis.com/venda/minas-gerais/belo-horizonte/apartamento/?pagina= + itr 

OBS: Esse o crawler extrai as informações importantes por meio do do json da página que é mais eficiente do que realizar tal tarefa interagindo com o java script. Para obter o json siga os seguintes passos: 
  1 - Abra o site https://www.netimoveis.com no google chrome,
  2 - Realize a busca que desejas,
  3 - Com a página do resultado da busca aberto, clique com o botão direito em alguma área em branco e selecione a opção inspecionar
  4 - Na aba network, dê um refresh na página (F5), aguarde o java script fazer as chamadas nas APIs do site e carregar o HTML. 
  5 - Após o carregamento, abra o segundo link da busca que contém a mensagem Json. 
  6 - Remova todas as informações no link após "?pagina=1" e cole esse link na linha sete do código sem o numero. Pois esse será iterado. 
