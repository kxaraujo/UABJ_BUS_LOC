def application(environ, start_response):
    # ... lógica para processar a requisição e gerar a resposta ...
    status = "200 OK"
    headers = [("Content-Type", "text/html")]

    # O corpo da resposta é geralmente uma string ou uma lista de bytes
    response_body = "Hello, World!"

    # Chamando a função start_response para iniciar a resposta
    start_response(status, headers)

    # Retornando o corpo da resposta
    return [response_body.encode()]
