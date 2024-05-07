
![Sun](src/app/static/images/sun-today.png)

# API Sunset-Sunrise

![GitHub last commit](https://img.shields.io/github/last-commit/HelmoFilho/Image-Server-OpenCV)

## Descrição

Este projeto tem como intuito a utilização da API [Sunset e Sunrise][Sunset-Sunrise Org] para mostrar o tempo restante até o proximo '*sunset*' ou '*sunrise*, a data que o evento ocorrerá e a data que a requisição foi feita. 

A resposta tem o seguinte schema:

```shell
{
    "description": "Request occurred successfully",
    "data": {
        "remaing_time": "23:24:41",
        "event_datetime": "27-02-2024 18:38:55",
        "request_datetime": "26-02-2024 19:08:13"
    }
}
```

## Build e Run

Antes de construir a imagem do Docker, certifique-se de que o Docker está disponível no seu ambiente. Execute o seguinte comando a partir do diretório do projeto pai:

```shell
docker build -t voxus-api .
```

Esse comando criará uma imagem Docker nomeada 'voxus-api'.

Para rodar a aplicação 'voxus-api' execute o seguinte comando pelo terminal:

```shell
docker run -d -p 15000:20000 voxus-api
```

Esse comando rodará o container na porta 15000 da maquina local. A partir dela se pode utilizar a api.

## Testes

Para rodar os testes unitarios entre no terminal dentro do container e digite:

```shell
pytest
```

será feito um pequeno relatorio mostrando quais testes passaram ou não.

## Documentação

A documentação pode ser acessada a partir dos seguintes endpoints:

- Formato Swagger
    - Utilizando o endpoint "/docs"

- Formato Redoc
    - Utilizando o endpoint "/redoc"


## Referência

 [Sunset-Sunrise Org]: https://sunrise-sunset.org/api
 - [Sunset-Sunrise Org](https://sunrise-sunset.org/api)
