# Evolução e escolha das perguntas

## ❓ Perguntas Originais
1. ~~Como a quarentena influenciou a taxa de evasão? (no geral e por cota)~~
2. Como evoluiu a declaração étnica ao longo do tempo?
3. Como evoluiu o perfil étnico da universidade ao longo do tempo, em particular no pré, durante e pós pandemia?
4. Qual é a relação entre a cota de ingresso dos alunos e sua região (estado/sub-região?) de origem?
5. A quarentena influenciou a diversidade regional dos alunos? Se sim, como?
6. A quarentena influenciou a diversidade de sexo biológico dos alunos? Se sim, como?
7. ~~Qual foi a influência da pandemia no coeficiente de rendimento acadêmico por curso? (baseando-se no ano de ingresso dos alunos)~~
8. Como a demanda por curso foi afetada pela passagem do tempo e pela pandemia?
9. ~~Como é o perfil dos alunos que evadiram ao longo do tempo e por curso? (no geral e atributos específicos)~~
10. Qual é o tempo de permanência média por curso ao longo do tempo? (destaque para a pandemia)
11. ~~Como é o perfil dos alunos de cada campus nos anos analisados?~~
12. Como evoluíram as notas do enem por curso ao longo do tempo (por ano)? E como foi essa evolução por contas?
13. Como é a média do CR por curso e por ano?
14. Qual campus recebe mais pessoas de fora do estado de Minas Gerais?
15. O tempo de duração definido para cada curso condiz com a media de duração gasto pelos alunos?

Observação: as linhas riscadas são as perguntas que foram descartadas, gerando 11 questões que foram as que o grupo escolheu para efetivamente responder

## Respostas da Issue do Github (primeira entrega)

1. ~~O que seria influenciar? evasão? maior número de reprovação?~~
2. Façam essa análise por porcentagem. (quantidade de alunos declarados pela quantidade total de alunos). O que seria declaração étnica?
3. Está relacionado ao aumento do número de vagas?
4. De onde vocês vão pegar os dados de estado/sub-região? IBGE?
5. Como vão medir essa influência? O que é a diversidade regional? subregional ou regional? Será que existe diversidade regional?
6. Como vão medir essa diversidade?
7. ~~Vão fazer teste de hipótese? Como vão medir essa influência? A base não tem o histórico acadêmico do aluno antes e depois da pandemia~~
8. Vão fazer teste de hipótese?
9. ~~O que é o "perfil" do aluno?~~
10.  OK
11.  ~~O que é o "perfil" do aluno?~~
12.  OK
13.  OK
14.  OK
15.  OK.
OBS.: Pergunta 5 e 6: Influência é a comparação? Se sim, vão fazer teste de hipótese para medir a significância da diferença da distribuição dos dados nos dois períodos?
Pergunta 14: Seria interessante analisar por curso
****
Código: OK, façam um relatório de mudanças aos poucos para eu acompanhar a evolução, pode ser em topicos para simplificar e para vocês não se perderem depois

## Nossas soluções para a Issue

1. Dentro da ufv (plotar gráficos para ver se compensa separar cursos e campus)
Analise dos 10 anos antecedentes a pandemia
Analise da data de saída entre 2020 e 2022 (pandemia) junto com a respsectiva situação ou código da situação (símbolos:saida A, T - continuidade: C, N ) Códigos chaves: saída e trancamento

2. Declaração racial na 2 (Plotar gráfico para ver essa evolução, 2012 surgiu o sistema de cotas olhar como isso influencia. TAlvez usar o termo identidade etnica, visto que as pessoas começaram a se declarar mais, ou seja, se identificar com o que são (nao sei se faz sentido)

Declaração Etnica: o que o individuo declarou durante a inscrição (preto, branco, amarelo, etc)

3. perfil étnico está relacionado ao aumento número de vagas para cotas? 

nao entendi >> quanto mais demanda de alunos, mais vagas, mais cotas, mas o perfil étnico-racial pode ser maior independente de cotas 

4. Pegar dados do IBGE de qual é a distribuição etnica por estado/regiao (definir um)

5. "Caso exista, a quarentena influenciou a diversidade regional dos alunos? Se sim, como?"
Diversidade seria os perfis que se encaixam em alguma cota -- nao seria regional zeria subregional (seria estado

qual diversificado são as cidades natais dos alnos que vieram para a UFV


6. Plotar gráfico, olhar médias e desvios padrões
Vai analisar o percentual alunos de cada sexo % total de alunos  (em cada período antes e pós pandemia
Pegar a msm quantidade de anos só pra comparação
Ex pegar 2020 a 2024
E 2015 a 2019
Talvez fazer isso por curso, visto que não será tão dificil

============================
TERMINAR DE REVISAR E COMPLEMENTAR ↓

7. Tatar os alunos de cada ano como uma única população, independente de quando entraram, quando vão formar.  os anos anteriores tendem a manter o mesmo padrão de entradas e saídas, não tendo que levar em conta a situação. Fazer o mesmo pra pandemia

8. Analisar gráficos, observar se houve miigração entre cursos, fazer comparação entre a amostra pós pandemia e pré pandemia. Como alguns grupos de pessoas pegaram as duas fazes (pre e pos pandemia) deve-se tratar para talvez tirar essas amostras enviesadas (tbm analisar não somente a entrada no curso, mas tbm a saída, já que pessoas que já estavam cursando podem ter saído por conta da pandemia)

9. Perfil pela análise de cotas e CRA e nota do enem (decidir como avaliar isso)
10. 

11. igual 9



5-6 = A quarentena começou efetivamente em 2020/2, então pegaríamos os dados dai em diante apenas dos ingressantes. Amostras bases de comparação: antes de 2020/2 e depois de 2020/2. Nesse caso não há problema avaliar somente ingressantes, pois a região e sexo não vão mudar após a pandemia (vamos assumir que os alunos não vao mudar de região)


14. % do total de alunos
15. coluna de formado - coluna de entrou - tempo do curso(teria que ter uma tabela dos tempos???) = 0


## Respostas Parte 2

### Critérios

Nota do critérios: 0 a 1

Q1 - Visualização de dados coerente (tipo)
Q2 - Organização do gráfico (disposição de texto, cor, escala)
Q3 - Análise e compreensão dos resultados 
Q4 - Discussão dos resultados
Q5 - Rigor estatístico
Q6 - Organização do Código

### Notas

Q1: 0.8
Q2: 0.7
Q3: 0.5
Q4: 0.5
Q5: 0.5
Q6: 1

### Comentários

#### Comentários Gerais:

- Faltou análise e conclusões sobre os gráficos.

#### Comentários Específicos:

+ Código separado. Senti falta de um README para entender o que cada arquivo faz.
Resposta 1: ??
Resposta 2: Sem análise, apenas gráfico. Gráfico estilizado e bem apresentado
Resposta 3: Apenas plot dos gráficos, sem uma comparação
Resposta 4: Existe alguma diferença significativa da distribuição de cada região?
Resposta 5: Gráfico confuso. Quase não percebi que o primeiro gráfico era de região e o segundo de estados. Qual foi a conclusão? Quarentena influenciou? respondeu a pergunta?
Resposta 6: Existe diferença estatisticamente significativa? Gráfico pobre visualmente e análise bem simples.
Resposta 7: ??
Resposta 8: Uma tabela sobre o que? Não entendi. Só printa a pré-pandemia
Resposta 9: ??
Resposta 10: O que é o identificador no gráfico? Em geral aumentou o tempo ou ficou a mesma coisa?
Resposta 11: ??
Resposta 12: O que os gráficos querem me dizer?
Resposta 13: Melhor análise do trabalho. teve um carinho para entender o que era o ano 0.
Resposta 14: O que os gráficos querem me dizer? Qual é a conclusão?
Resposta 15: O que a tabela quer me dizer? Qual é a conclusão?


1. Como a quarentena influenciou a taxa de evasão? (no geral e por cota)
2. Como evoluiu a declaração étnica ao longo do tempo?
3. Como evoluiu o perfil étnico da universidade ao longo do tempo, em particular no pré, durante e pós pandemia?
4. Qual é a relação entre a cota de ingresso dos alunos e sua região (estado/sub-região?) de origem?
5. A quarentena influenciou a diversidade regional dos alunos? Se sim, como?
6. A quarentena influenciou a diversidade de sexo biológico dos alunos? Se sim, como?
7. Qual foi a influência da pandemia no coeficiente de rendimento acadêmico por curso? (baseando-se no ano de ingresso dos alunos) 
8. Como a demanda por curso foi afetada pela passagem do tempo e pela pandemia?
9. Como é o perfil dos alunos que evadiram ao longo do tempo e por curso? (no geral e atributos específicos)
10. Qual é o tempo de permanência média por curso ao longo do tempo? (destaque para a pandemia)
11. Como é o perfil dos alunos de cada campus nos anos analisados?
12. Como evoluíram as notas do enem por curso ao longo do tempo (por ano)? E como foi essa evolução por contas?
13. Como é a média do CR por curso e por ano?
14. Qual campus recebe mais pessoas de fora do estado de Minas Gerais?
15. O tempo de duração definido para cada curso condiz com a media de duração gasto pelos alunos?
