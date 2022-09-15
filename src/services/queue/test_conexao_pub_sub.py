from publisher import Publisher

P = Publisher()

while True:
    mensagem = input('Digite a mensagem: ')
    P.publish('meu_topico.aa', f'"{mensagem}"')