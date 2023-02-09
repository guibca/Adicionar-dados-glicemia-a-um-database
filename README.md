# Adicionar-dados-de-glicemia-a-um-database
Este projeto adiciona valores de glicemia em um banco de dados para fins de armazenamento e criação de dashboards.

No arquivo CSV são armazenadas duas informações:

		(a) glic_valor: Valor do índice de açucar no sangue em mg/dl.

		(b) glic_data: Data e hora da coleta, armazenada em formato timestamp.
 
Estas duas informações são inseridas frequentemente no arquivo CSV a cada vez que o usuário realiza uma leitura de sua glicemia.
Tais dados são obtidos por meio de uma automação do aplicativo Apple Shortcuts a qual solicita um input com o valor da glicemia, retornando a seguinte informação:

		[valor da glicemia],[data e hora atual]
  
Deste modo, tem-se um arquivo CSV semelhante ao modelo abaixo para ser lido por meio deste script em Python:
		
		glic_valor,glic_data
		64,2023-02-07 19:02:54
		135,2023-02-07 23:20:19
		126,2023-02-08 01:12:42
		103,2023-02-08 08:05:04
		139,2023-02-08 11:03:11
		
A motivação deste projeto foi permitir a visualização dos valores de minha glicemia com o fim de fortalecer o controle glicemico, contribuindo para o tratamento de minha diabetes tipo 1.

Deste modo, foi possível gerar insights uteis do comportamento de minha glicemia por meio de uma dashboard constuida utilizando o software Tableau. Tal dashboard é apresentada em consultas médicas quando necessário, permitindo que médicos também acompanhem o controle de minha diabetes tipo 1 de forma facilitada.


