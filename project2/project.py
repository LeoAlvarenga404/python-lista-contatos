def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
  
  contato = {
    'Contato': nome_contato,
    'Telefone': telefone_contato,
    'Email':email_contato,
    'Favorito': False
    }
  contatos.append(contato)
  print(f'contato do(a) {nome_contato} foi adicionado')
  return

def ver_contatos(contatos):
  print('\n Lista de contatos:')
  for indice, contato in enumerate(contatos, start=1):
    status = '★ ' if contato['Favorito'] else ''
    nome_contato = contato['Contato']
    telefone_contato = contato['Telefone']
    email_contato = contato['Email']
    
    print(f'{indice}: {status}{nome_contato} - {telefone_contato} - Email:{email_contato}')
  return

def ver_contatos_favoritos(contatos):
  print('\n Lista de contatos favotiros:')
  for indice, contato in enumerate(contatos, start=1):
    if contato['Favorito']:
      nome_contato = contato['Contato']
      telefone_contato = contato['Telefone']
      email_contato = contato['Email']
      print(f'{indice}: {nome_contato} - {telefone_contato} - Email:{email_contato}')
  return

def editar_contato(contatos, indice, novo_nome_contato=None, novo_telefone_contato=None, novo_email_contato=None):
  indice_ajustado = int(indice) - 1
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    if novo_nome_contato:
        contatos[indice_ajustado]['Contato'] = novo_nome_contato
    if novo_telefone_contato:
        contatos[indice_ajustado]['Telefone'] = novo_telefone_contato
    if novo_email_contato:
        contatos[indice_ajustado]['Email'] = novo_email_contato
  return
 
def favoritar_ou_desfavoritar_contato(contatos, indice):
  indice_ajustado = int(indice) - 1
  contato = contatos[indice_ajustado]
  if contato['Favorito']:
    contato['Favorito'] = False
    print(f'Contato {indice_ajustado + 1} desfavoritado')
  else:
    contato['Favorito'] = True
    print(f'Contato {indice_ajustado + 1} favoritado')

def apagar_contato(contatos, indice):
  indice_ajustado = int(indice) - 1
  del contatos[indice_ajustado]
  return 

contatos = []

while True:
  print('Esta é seu gerenciador de contatos!\n')
  print('1. Adicionar contato')
  print('2. Ver contatos')
  print('3. Editar um contato')
  print('4. Favoritar/Desfavoritar um contato')
  print('5. Ver contatos favoritos')
  print('6. Apagar um contato')
  print('7. Sair')

  escolha = input('Digite uma opção: ')

  
  if escolha == '1':
    nome_contato = input('Digite o nome do contato: ')
    telefone_contato = input('Digite o número do contato: ')
    email_contato = input('Digite o email do contato: ')
    adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    
  elif escolha == '2':
    ver_contatos(contatos)
  
  elif escolha == '3':
    ver_contatos(contatos)
    indice = input('Digite o número do contato que deseja editar')
    novo_nome_contato = input('Digite o novo nome do contato')
    novo_telefone_contato = input('Digite o novo número do contato')
    novo_email_contato = input('Digite o novo email do contato')
    editar_contato(contatos,indice,novo_nome_contato,novo_telefone_contato,novo_email_contato)
    
  elif escolha == '4':
    ver_contatos(contatos)
    indice = input('Digite o número do contato que deseja favoritar/desfavoritar')
    favoritar_ou_desfavoritar_contato(contatos, indice)
  
  elif escolha == '5':
    ver_contatos_favoritos(contatos)
    
  elif escolha == '6':
    ver_contatos(contatos)
    indice = input('Qual contato você quer apagar?: ')
    apagar_contato(contatos,indice)
  elif escolha == '7':
    break

print('Gerenciador de contatos finalizado.')
2