# Adicionar-dados-de-glicemia-a-um-database
Este projeto adiciona valores de glicemia em um banco de dados para fins de armazenamento e criação de dashboards.

No arquivo CSV são armazenadas duas informações:

		(a) glic_valor: Valor do índice de açucar no sangue (glicemia) em mg/dl.

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
		
Finalizada a leitura do arquivo CSV, os dados são inseridos no banco de dados MySQL, hospedado em um servidor local.

Por fim, executa-se uma consulta SQL para tratar os dados, classificando o valor da glicemia bem como o horário do dia em que a leitura ocorreu, resultando na seguinte tabela final: 

<img width="663" alt="image" src="https://user-images.githubusercontent.com/124844502/218586321-8f88b317-594b-42ad-b274-c38cc90a7946.png">


Com as informações dispostas na tabela final, foi construída a dashboard abaixo, utilizando a ferramenta Tableau:


<img width="1157" alt="image" src="https://user-images.githubusercontent.com/124844502/232182218-bd84d2a5-dd37-4e19-af4f-b6b6416bc84a.png">


A dashboard está conectada ao banco de dados MySQL, deste modo, as informações são atualizadas sempre que o script Python é executado.

Assim, foi possível gerar insights uteis do comportamento de minha glicemia por meio do acompanhamento da dashboard constuida com o Tableau. Tal arquivo é apresentado em consultas médicas quando necessário, permitindo que médicos tamém acompanhem o controle de minha diabetes tipo 1.

A motivação deste projeto foi permitir a visualização dos valores de minha glicemia com o fim de fortalecer meu controle glicemico, contribuindo para o tratamento de minha diabetes tipo 1.
