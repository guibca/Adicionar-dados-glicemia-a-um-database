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
		
Finalizada a leitura do arquivo CSV, os dados são inseridos no banco de dados MySQL, hospedado em um servidor local.

Por fim, executa-se uma consulta SQL para tratar os dados, classificando o valor da glicemia bem como o horário do dia em que a leitura ocorreu.
Deste modo, a tabela final, gerada por meio do arquivo CSV é a seguinte: 

Abaixo é apresentado a dashboard construida com os dados coletados, utilizando a ferramenta Tableau:

<img width="1440" alt="Captura de Tela 2023-02-08 às 23 47 06" src="https://user-images.githubusercontent.com/124844502/217704873-b41be0ec-2879-4925-8353-f0daaa01d54c.png">

A dashboard está conectada à um banco de dados MySQL, hospedado num servidor local, deste modo, as informações nela presentes são atualizadas sempre que o script Python é executado.

Deste modo, foi possível gerar insights uteis do comportamento de minha glicemia por meio de uma dashboard constuida utilizando o software Tableau. Tal dashboard é apresentada em consultas médicas quando necessário, permitindo que médicos também acompanhem o controle de minha diabetes tipo 1 de forma facilitada.

A motivação deste projeto foi permitir a visualização dos valores de minha glicemia com o fim de fortalecer meu controle glicemico, contribuindo para o tratamento de minha diabetes tipo 1.

Como projeto futuro, espero fortalecer minhas habilidades para desenvolver um aplicativo web com estas funcionalidades implantadas, permitindo que pessoas que se encontram "no escuro" em relação ao controle de seu diabetes, possam ser ajudadas com a visualização de seus dados de glicemias apurados.
