import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#1. CRIE UMA TABELA CHAMADA 'ALUNOS' COM OS SEGUINTES CAMPOS: ID (INTEIRO), NOME(TEXTO), IDADE(INTEIRO) E CURSO(TEXTO)
#conexao.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. INSIRA PELO MENOS 5 REGISTROS DE ALUNOS NA TABELA QUE VOC~E CRIOU NO EXERCICIO ANTERIOR
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Laura", 23, "Letras")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Fernando", 21, "Matemática")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Wilson", 30, "Engenharia Aeroespacial")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Lethycia", 24, "Engenharia de Gestão")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Laryssa", 25, "Ciência de Dados")')

#3. consultas basicas
# a) selecionar todos os registros da tabela aluno

#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#    print(alunos)

# b) selecionar o nome e a idade dos alunos com mais de 20 anos

#idade_maior20 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
#for alunos in idade_maior20:
#    print(alunos)

# c) selecionar os alunos do curso de Engenharia em order alfabética

#engenharia = cursor.execute('SELECT * FROM alunos WHERE curso LIKE "Engenharia%" ORDER BY nome ASC')
#for alunos in engenharia:
#    print(alunos)

#d) contar numero total de alunos na tabela
#alunostotal = cursor.execute('SELECT COUNT(*) FROM alunos')
#for total in alunostotal:
#    print(total[0])

# 4. atualização e remoção
#a) atualize a idade de um aluno específico na tabela
#cursor.execute('UPDATE alunos SET idade=19 WHERE nome = "Laura"')

#b) remova um aluno peço seu ID
#cursor.execute('DELETE from alunos WHERE id = 5')

# 5. criar uma tabela e inserir dados. Crie uma tabela chamada 'clientes' com os campos ID (chave primaria), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de cliente4s na tabela
#conexao.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Laura", 19, 258.4)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Fernando", 21, 758.8)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Wilson", 30, 587.3)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Lethycia", 24, 4567.9)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "José", 53, 3582.9)')

# 6. CONSULTAS E FUNÇÕES AGREGADAS. Escreva consultas sql para realizar as seguintes tarefas:
# a) selecione o nome e a idade dos clientes com idade superior a 30 anos:
#cliente30 =cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for clientes in cliente30:
#       print(clientes)

#b) calcule o saldo médio dos clientes
#saldomedio = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for saldo in saldomedio:
#       print(saldo[0])

#c) encontre o cliente com saldo máximo
#saldomax = cursor.execute('SELECT nome FROM clientes ORDER BY saldo DESC LIMIT 1')
#for saldo in saldomax:
#       print(saldo[0])

#d) conte quantos clientes têm saldo acima de 1000
#qtdclientes = cursor.execute('SELECT COUNT(nome) from clientes WHERE saldo > 1000')
#for clientes in qtdclientes:
#       print(clientes[0])

# 7. ATUALIZAÇÃO E REMOÇÃO COM CONDIÇÕES
#a) atualize o saldo de um cliente específico
#cursor.execute('UPDATE clientes SET saldo = 1345.6 WHERE nome = "Wilson"')

#b) Remova um cliente pelo seu ID
#cursor.execute('DELETE FROM clientes WHERE saldo < 300')

#8. JUNÇÃO DE TABELAS
# crie uma segunda tabela chamada compras com os campos:
# ID, cliente_id, produto e valor. Insira algumas compras associadas a clientes existentes na tabela 'clientes'
#escreva uma consulta pra exibir o nome do cliente, o produto e o valor de cada compra

#cursor.execute('CREATE TABLE compras (id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT);')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 2, "Celular", 2585.4)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 4, "Geladeira", 4657.4)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 2, "Fogão", 1765.9)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 5, "Vara de Pescar", 564.1)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5, 3, "Whey de Chocolate", 167.9)')

dadosclientes = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')
for clientes in dadosclientes:
       print(clientes)


conexao.commit()
conexao.close