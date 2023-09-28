from src.service.service_user import ServiceUser
class TestServiceUser:

    #Add With success Test
    def test_add_user_with_sucess(self):
        service = ServiceUser()
        resposta_esperada = "Usuário adicionado"

        resposta = service.add_user("Sabrina", "QA")

        assert resposta_esperada == resposta

    #Name Failure Tests
    def test_add_user_failed_name_none(self):
        service = ServiceUser()
        resposta_esperada = "Usuário inválido"

        resposta = service.add_user(None, "QA")

        assert resposta_esperada == resposta
    def test_add_user_failed_existent_name(self):
        service = ServiceUser()
        service.add_user("Sabrina", "QA")
        resposta_esperada = "Usuário já existe!"

        resposta = service.add_user("Sabrina", "QA")

        assert resposta_esperada == resposta

    #Remove with sucess test
    def test_remove_user_with_sucess(self):
        service = ServiceUser()
        service.add_user("Sabrina", "QA")
        resposta_esperada = "Usuário removido!"

        resposta = service.remove_user("Sabrina", "QA")

        assert resposta_esperada == resposta

    #Remove Failure Tests
    def test_remove_user_failed_inexistent_user(self):
        service = ServiceUser()
        service.add_user("Sabrina", "QA")
        resposta_esperada = "Usuário não existe!"

        resposta = service.remove_user("Palita", "QA")

        assert resposta_esperada == resposta

    def test_remove_user_failed_user_job_none(self):
        service = ServiceUser()
        service.add_user(None, None)
        resposta_esperada = "Usuário inválido"

        resposta = service.remove_user(None, None)

        assert resposta_esperada == resposta

    #Update with sucess test
    def test_udate_user_name_with_sucess(self):
        service = ServiceUser()
        service.add_user("Sabrina para Atualizar", "QA")
        resposta_esperada = "Usuário atualizado: Sabrina Barbosa"

        resposta = service.update_user_name("Sabrina para Atualizar", "QA", "Sabrina Barbosa")

        assert resposta_esperada == resposta

    #Update Failure Tests
    def test_update_user_name_failed_user_job_none(self):
        service = ServiceUser()
        service.add_user(None, None)
        resposta_esperada = "Usuário inválido"

        resposta = service.update_user_name(None, "QA", None)

        assert resposta_esperada == resposta

    #Get by name with sucess test
    def test_get_user_by_name_with_sucess(self):
        service = ServiceUser()
        service.add_user("Sabrina Barbosa", "QA")
        resposta_esperada = "Sabrina Barbosa"

        resposta = service.get_user_by_name("Sabrina Barbosa", "QA")

        assert resposta_esperada == resposta

    #Get by name Failure Tests
    def test_get_user_by_name_failed_name_none(self):
        service = ServiceUser()
        service.add_user(None, None)
        resposta_esperada = "Usuário inválido"

        resposta = service.get_user_by_name(None, None)

        assert resposta_esperada == resposta
