# API para controle de leads

Lead: São pessoas que podem estar interessados em algum tipo de produto ou serviço. Esses possíveis futuros clientes podem ser coletados através de preenchimento de formulários ou cliques em páginas da internet, os dados geralmente são utilizados em campanhas publicitárias.

O objetivo principal e fazer o CRUD de cada lead, o usuario podera criar, ler, editar e excluir a lead caso deseje.

## Buscar por todas leads

### Request

`GET /leads`

    https://api-crud-leads.herokuapp.com/leads

### Response

    [
        {
            "name": "John Doe",
            "email": "john@emsil.com",
            "phone": "(41)90020-0000",
            "creation_date": "Fri, 11 Feb 2022 12:36:10 GMT",
            "last_visit": "Fri, 11 Feb 2022 12:36:10 GMT",
            "visits": 1
        }
    ]

## Criar uma lead

#### Request

`POST /leads`

    http:https://api-crud-leads.herokuapp.com/leads

#### Body

    {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
    }

#### Response

    {
        "name": "John Doe",
        "email": "john@email.com",
        "phone": "(41)90000-0000",
        "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
        "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
        "visits": 1
    }

## Tipo de erros ao criar uma lead

### ValueError caso telefone não esteja no formato adequado

#### Request

    {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "41900000000"
    }

#### Response

    {"error": "O campo Phone deve ser no formato (xx)xxxxx-xxxx"}

### KeyError caso phone, name ou email não seja passado.

#### Request

    {
    "name": "John Doe",
    "phone": "(41)90000-0000"
    }

#### Response

    {"error": "Os campos 'name, email, phone' são obrigatórios"}

### IntegrityError caso o email já conste no sistema

#### Request

    {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
    }

#### Response

    {"error": "esse email já está cadastrado"}

## Atualizar a visita da lead

#### Request

`PATH /leads`

    http:https://api-crud-leads.herokuapp.com/leads

#### Body

    {
    "email": "john@email.com"
    }

#### Response

    {
        "name": "John Doe",
        "email": "john@emsil.com",
        "phone": "(41)90020-0000",
        "creation_date": "Fri, 11 Feb 2022 12:36:10 GMT",
        "last_visit": "Wed, 23 Feb 2022 19:19:36 GMT",
        "visits": 2
    }

## Tipo de erros ao tentar atualizar uma lead

### NoResultFound caso o email não for encontrado

#### Request

    {
    "email": "jonathan@email.com",
    }

#### Response

    {"error": "o Email informado não foi encontrado"}

### KeyError caso o email não for passado

#### Request

    {
    "emayl": "john@email.com",
    }

#### Response

    {"error": "O campo email é obrigatório"}

### FormatError caso o email passado não for string

#### Request

    {
    "email": 1,
    }

#### Response

    {"error": "Formato esperado {'email':string}"}

`DELETE /leads`

    http:https://api-crud-leads.herokuapp.com/leads

#### Body

    {
    "email": "john@email.com"
    }

#### Response

    NO RESPONSE

## Tipo de erros ao tentar Deletar uma lead

### NoResultFound caso o email não for encontrado

#### Request

    {
    "email": "jonathan@email.com",
    }

#### Response

    {"error": "o Email informado não foi encontrado"}

### KeyError caso o email não for passado

#### Request

    {
    "emayl": "john@email.com",
    }

#### Response

    {"error": "O campo email é obrigatório"}

### FormatError caso o email passado não for string

#### Request

    {
    "email": 1,
    }

#### Response

    {"error": "Formato esperado {'email':string}"}
