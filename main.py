from src.service.service_user import ServiceUser

service = ServiceUser()

resposta = service.add_user(name="Sabre", job="Eng")
print(resposta)

resposta = service.remove_user(name="Sabre", job="Eng")
print(resposta)

resposta = service.update_user(name="Sabrina", job="QA")
print(resposta)
