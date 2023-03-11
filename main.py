import subprocess
import time

def limpartela():
  subprocess.run("clear", shell= True)

def Load():
  for i in range(4):
    print("Loading{}".format("."*i))
    time.sleep(0.5)
    limpartela()


Load()
print("-----      R E G I S T E R     -----")
i = 0; banco = {} ; key = 0; 
while i < 1:
  dados = {}
  
  while i < 1:
    nome = str(input("  Nome: "))
    if len(nome) < 15:
      dados.setdefault("Nome", nome)
      break
    else:
      print("  # Nome errado")

# Verificação de Email
      
  while i < 1:
    email = str(input("  Email: "))
    ver_email = email[email.find("@"):email.find(".", email.find("@"), len(email))]
    
    if ver_email.lower() == "@outlook" or ver_email.lower() == "@gmail" or ver_email.lower() == "@hotmail":
      dados.setdefault("Email", email)
      break
    else:
      print("  # email inválido")
      
# Verificação de senha
      
  i_senha = 0
  while i_senha < 1:
    senha = input("  Senha: ")
    
    if len(str(senha)) < 12 and len(str(senha)) > 5:
      i_conf = 0
      while i_conf < 1:
        conf_senha = input("  Confirmar Senha: ")
        
        if conf_senha == senha:
          dados.setdefault("Senha", senha)
          i_conf += 1
          i_senha += 1 
        else:
          print("  # senha incorreta")    
    else:
      print("  # A senha deve ter no mínimo 5 e no máximo 8 caracteres.")
    
# id banco
  
  key += 1
  banco.setdefault(key, dados)
  
  ciclo = input("  # Deseja continuar o registro: ")

  if ciclo.lower() == "não" or ciclo.lower() == "nao" or ciclo.lower() == "n":
    i+= 1
    limpartela()
  else:
    print(" ")
    print("  # {} Finalizado --------------------------- ".format(key))
    
    continue
  
else:
  for i in banco.items(): 
    print(i)
  
# Login!
    
i_login = 0
print("-----      L O G I N     -----")
while i_login < 1:
  User = input("  User: ")
  password = input("  Password: ")

  
  for key in banco:
    if User == banco.get(key).get("Nome") and password == banco.get(key).get("Senha"):
      limpartela()
      Load()
      print("  Entrada Concluida!!")
      x = banco.get(key).get("Nome"); y = banco.get(key).get("Senha")
      i_login += 1
      time.sleep(1)
      limpartela()
    
else:
  print("  User: {} | Password: {} ".format(x, y))
  