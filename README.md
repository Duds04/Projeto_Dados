## Sumário
- [TRABALHO ANÁLISE DE DADOS ENFOQUE NA PANDEMIA](#trabalho-análise-de-dados-enfoque-na-pandemia)
  - [😎 Alunos](#-alunos)
  - [🎯 Objetivos](#-objetivos)
  - [✍️ Introdução](#️-introdução)
  - [❓ Perguntas](#-perguntas)
    - [Escolha das perguntas](#escolha-das-perguntas)
  - [💭 Coluna código\_situação](#-coluna-código_situação)
  - [Modalidades cotas](#modalidades-cotas)
  - [🚦 Organização do trabalho](#-organização-do-trabalho)
    - [Pasta src](#pasta-src)
- [🔍 Overview do Trabalho](#-overview-do-trabalho)
  - [Tratamento de dados](#tratamento-de-dados)
  - [Respostas as perguntas](#respostas-as-perguntas)
- [Referências](#referências)

# TRABALHO ANÁLISE DE DADOS ENFOQUE NA PANDEMIA 

A análise dos dados foi especificada no notebook a seguir: [link notebook](./Trabalho_CDD.ipynb)
## 😎 Alunos
- Guilherme Broedel Zorzal - 5064 - [GuilhermeZorzal](https://github.com/GuilhermeZorzal)
- Eduardo Antunes dos Santos Vieira - 5076 - [eduardo-antunes](https://github.com/eduardo-antunes)
- Maria Eduarda de Pinho Braga - 5099 -  [Duds04](https://github.com/Duds04)
- João Gabriel Angelo Bradachi - 5078 - [JBradachi](https://github.com/JBradachi)

## 🎯 Objetivos 

O seguinte trabalho prático têm por objetivo analisar e tirar conclusões acerca dos alunos da Universidade Federal de Viçosa. 

## ✍️ Introdução
A UFV é uma grande universidade, com grande diversidade e alunos vindos de diversos contextos e realidades. A partir de dados como etnias, renda, coeficiente de rendimento, local de origem, etc é possível explorar tais diferenças e singularidades, podendo encontrar conhecimentos úteis que podem, inclusive, melhorar a vida desses alunos e ajudá-los em sua caminhada pelo ensino superior e sua formação. 

Tendo isso em vista, este trabalho visou levantar e explorar essas perguntas que possivelmente tragam informações relevantes sobre os alunos. Algumas perguntas têm o enfoque específico a pandemia que foi um período que marcou significadamente uma variação no processos da faculdade. 

## ❓ Perguntas 

1.  Como evoluiu a declaração étnica ao longo do tempo?
2.  Como evoluiu o perfil étnico da universidade ao longo do tempo, em particular no pré, durante e pós pandemia?
3.  Qual é a relação entre a cota de ingresso dos alunos e sua região (estado/sub-região?) de origem?
4.  A quarentena influenciou a diversidade regional dos alunos? Se sim, como?
5.  A quarentena influenciou a ingreso mais diverso de alunos em relação ao gênero no curso de Ciência da Computação? Se sim, como?
6.  Como a demanda por curso foi afetada pela passagem do tempo? E pela pandemia?
7.  Qual é o tempo de permanência média por curso ao longo do tempo? (destaque para a pandemia)
8.  Como evoluíram as notas do enem por curso ao longo do tempo (por ano)? E como foi essa evolução por contas?
9.  Como é a média do CR por curso e por ano?
10. Qual campus recebe mais pessoas de fora do estado de Minas Gerais?
11. O tempo de duração definido para cada curso condiz com a media de duração gasto pelos alunos?

### Escolha das perguntas

Inicialmente o grupo havia escolhido 15 perguntas, que podem ser conferidas no arquivo [Perguntas e Respostas](./PerguntasERespostas.md). Esse arquivo possui as issues geradas no Github e as atualização feitas para resolução das questões. 

Após a primeira entrega, o grupo decidiu ficar com as 11 questões apresentadas acima

## 💭 Coluna código_situação

Uma das colunas do conjunto de dados é a `Codigo_Situacao_Aluno`, que apresenta diversos valores. O significados dos valores é dado pela tabela abaixo

| Símbolo    | Significado |
| -------- | ------- |
| A | Abandono |
| B | Concluiu, mas não colou grau |
| C | Conclusão |
| D | Desligamento |
| F | Falecimento |
| G | Afastamento/intercâmbio |
| H | Habilitação |
| I | Concluiu, mas o relatório não foi analisado |
| J | Matrícula temporariamente suspensa |
| K | Trancamento |
| M | Mudança de curso |
| N | Normal |
| Q | Matrícula condicional (desligamento reconsiderado) |
| R | Afastamento (desligamento reconsiderado) |
| T | Transferência |
| S | Anulamento de matrícula |
| W | Afastamento especial |
| X | Exclusão |
| Y | Afastamento |
| Z | Trancamento por motivo de saúde |

## Modalidades cotas

As modalidades abaixo foram retiradas diretamente do [Edital UFV SISU 2018](https://www2.pse.ufv.br/wp-content/uploads/2018/01/Edital-UFV-SISU-2018.pdf).
- MODALIDADE 1 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, autodeclarados pretos, pardos ou indígenas, com renda familiar bruta mensal igual ou inferior a 1,5 (um vírgula cinco) salário mínimo per capita. 
- MODALIDADE 2 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, autodeclarados pretos, pardos ou indígenas, com renda familiar bruta mensal igual ou inferior a 1,5 (um vírgula cinco) salário mínimo per capita e pessoa com deficiência. 
- MODALIDADE 3 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, que NÃO se autodeclaram pretos, pardos ou indígenas, com renda familiar bruta mensal igual ou inferior a 1,5 (um vírgula cinco) salário mínimo per capita. 
- MODALIDADE 4 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, que NÃO se autodeclaram pretos, pardos ou indígenas, com renda familiar bruta mensal igual ou inferior a 1,5 (um vírgula cinco) salário mínimo per capita e pessoa com deficiência. 
- MODALIDADE 5 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, autodeclarados pretos, pardos ou indígenas, independentemente da renda familiar. 
- MODALIDADE 6 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, autodeclarados pretos, pardos ou indígenas, independentemente da renda familiar e pessoa com deficiência. 
- MODALIDADE 7 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, que NÃO se autodeclaram pretos, pardos ou indígenas, independentemente da renda familiar. 
- MODALIDADE 8 – Candidatos que cursaram o ensino médio integralmente em escolas públicas brasileiras, que NÃO se autodeclaram pretos, pardos ou indígenas, independentemente da renda familiar e pessoa com deficiência. 
- MODALIDADE 9 – Candidatos de AMPLA CONCORRÊNCIA que serão classificados somente de acordo com as notas obtidas no ENEM 2017.  

## 🚦 Organização do trabalho 

Devido à alta quantidade de arquivos gerados durante a elaboração do trabalho, esses foram divididos em duas pastas principais:
- `Datasets` = É a pasta que contém todos os arquivos de dados utilizados durante o trabalho prático. Isso inclui o datasets com os dados dos alunos, que é o foco do trabalho, bem como outros datasets auxiliares utilizados para responder certas perguntas no trabalho.
- `src` = É a pasta que contém os arquivos `.py` e `.ipynb` criados durante o trabalho. Nele estão o tratamento dos dados e as análises feitas com base nas perguntas previamente formuladas pelo grupo

### Pasta src

A pasta `src` é a pasta que contém aquilo que foi utilizado de mais importante para realização das análises. Ela contém: 

- `Imagens` = Contém algumas imagens que foram utilizadas durante o trabalho para ilustrar melhor os resultados obtidos
- `Funcoes.py` = É um arquivo com algumas funções que foram utilizados durante o desenvolvimento do trabalho. A ideia por trás da criação de um arquivo com funções separadas é permitir que elas fossem usadas em qualquer arquivo, e não somente dentro do `.ipynb` em que ela foi criada
- Os arquivos `RespostasParte1.ipynb`, `Regressoes.ipynb` e `TratamentoDeDados.ipynb` são a parte principal do trabalho, e portanto serão explicados separadamentes adiante

![organizacao](src/Imagens/organizacao_tp.png)
  
# 🔍 Overview do Trabalho

Para a execução do trabalho e para uma boa organização d trabalho, foram utilizados um notebook Jupyter para cada tarefa que percebemos ser necessária realizar com o dataset. Os arquivos utilizados para essas análises e tratamentos são os contidos dentro do diretório `src`. 

## Tratamento de dados

Para que uma boa análise seja feita, é necessário que os dados estejam limpos e bem organizados. Porém o dataset original continha diversos problemas que precisavam ser resolvidos e padronizados, tais como problema de digitação e dados faltosos. Portanto, era necessário que o dataset original fosse submetido a uma limpeza.

O arquivo [`TratamentoDeDados.ipynb`](src/TratamentoDeDados.ipynb) foi o arquivo utilizado para realização do tratamento de dados. Todas as etapas realizadas estão explicadas dentro do arquivo, bem como algumas decisões importantes que foram tomadas. 

O único ponto que vale a pena ressaltar é que ao fim do tratamento, correção e enriquecimento do dataset, terminamos com algumas colunas que não existiam no dataset original, que são: 

- Area;
- Admissao_Ano;
- Admissao_Semestre;
- Saida_Ano;
- Saida_Semestre;

A coluna `area` contém a classificação dos cursos por área de conhecimento, enquando as colunas `Admissao_Ano`, `Admissao_Semestre`, `Saida_Ano`, `Saida_Semestre` são os anos de Saida e Admissao dividos em anos e semestre, para facilitar em algumas análises

O processo de obtenção das colunas foi devidamente explicado dentro do notebook.

## Respostas as perguntas
Principal, que que foi feito, foco em que tivemos, métodos usados, etc




# Referências

https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/38719-censo-2022-pela-primeira-vez-desde-1991-a-maior-parte-da-populacao-do-brasil-se-declara-parda

http://portal.mec.gov.br/component/tags/tag/politica-de-cotas#:~:text=A%20política%20de%20cotas%20foi,proposta%20foi%20aprovada%20por%20unanimidade.

https://www2.pse.ufv.br/wp-content/uploads/2018/01/Edital-UFV-SISU-2018.pdf