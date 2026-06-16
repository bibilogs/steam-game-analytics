A fase I do projeto final da disciplina de Programação para Dados consiste em utilizar os recursos da linguagem Python, incluindo o uso de listas, dicionários, arquivos, exceções, orientação a objetos e outros recursos discutidos durante as aulas para criar um programa que executa as consultas que respondam perguntas relacionados a um domínio de aplicação. Os critérios principais deste trabalho são: (i) exercitar o uso de arquivos e estruturas de dados como listas e dicionários; (ii) colocar em prática conceitos relacionados à orientação a objetos, (iii) praticar a elaboração de código-fonte de alta qualidade com uso de classes, documentação e testes. 


Em resumo, além de elaborar o código necessário para completar as tarefas solicitadas, devem ser aplicadas técnicas que aumentem a qualidade do código, principalmente, aumentem a legibilidade e a capacidade de manutenção a longo prazo. 
 

Nesta etapa, você deve: 
    Realizar a carga do conjunto de dados fornecido;
    Elaborar programas de alta qualidade;
    Responder as duas perguntas relacionadas ao conjunto de dados;
    Elaborar uma pergunta própria sobre o conjunto de dados;
    Responder as 3 perguntas através do uso de software desenvolvido na linguagem Python. Atenção Além da resposta estar correta, deve discorrer brevemente sobre os resultados obtidos (evite respostas curtas). 
 

 O universo de discurso da fase I e da fase II é o mesmo: jogos eletrônicos. A diferença é que na fase I é realizada uma análise exploratória e preliminar do arquivo de dados. Na fase I não podem ser utilizadas bibliotecas como numpy, matplotlib e pandas. Recomenda-se utilizar doctools e CSV reader, que são bibliotecas bastante populares. 
 

Devido à quantidade de dados extraídos da plataforma, a empresa está com dificuldades de organizar o código de maneira que o programa possa ser revisto e alterado no futuro para atender outras consultas e trabalhar com outras bases de dados de outros distribuidores como a Como um programador Epic e Paradox. 

 
Disposto a aceitar o desafio, você se oferece para propor uma estrutura que organize o código de maneira que ele possa ser importado e utilizado como uma biblioteca similar ao exemplo da Dyrapy apresentado em aula.  
 

Seu objetivo é esconder a complexidade de manipulação dos dados em um programa ou classe que possa ser utilizado por outro programador. 

 
Seu trabalho nesta fase é criar módulos, classes, métodos e exceções que apresentem uma interface de programação bem documentada e confiável. 

 
Para demonstrar seu trabalho, devem ser respondidas três perguntas, demonstrado a organização proposta: 

    Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma? 
    Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados. 
    Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta adicional deve ser proposta e respondida por você. 

TESTES 

Como você é um analista de dados dedicado, serão criados testes sobre uma amostra de 20 jogos do cadastro separados aleatoriamente em um arquivo. Não utilize os 20 jogos iniciais. A amostra deve ser criada uma vez, armazenada no disco e entregue juntamente com o código. 


A amostra deve ser processada manualmente ou com uso de uma planilha estatística para calcular as respostas das duas perguntas. Esse esforço adicional deve ser utilizado para gerar o resultado esperado no teste de cada método desenvolvido. O sistema deve executar sobre a amostra no caso de teste e sobre o arquivo completo quando fora de testes. Demonstre que o resultado calculado pelo sistema sobre a amostra é o mesmo resultado do cálculo determinado manualmente. Desta forma, temos uma maior confiança de que o sistema executa corretamente. 


Observe que a ênfase da fase I está em criar um código com alta qualidade interna. Para garantir que seu módulo é correto e completo, você criará um arquivo Jupyter Notebook (ou arquivos .py) contendo a implementação que gera as respostas para as três perguntas listadas acima e confere automaticamente se as respostas sobre a amostra são conforme esperadas. 