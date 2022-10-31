# Geral :world_map:	
Desenvolver um sistema web para fazer upload e armazenar arquivos (documentos de forma geral) criando um grande banco de dados com bastante armazenamento, que permita organizar, filtrar e disponibilizar para download esses arquivos. Além disso, ter uma parte de administração de colaboradores e banners da página inicial.


---------------------------------------------------------











































# Criação De Usuario :teacher:	
Cria usuarios do sistema

## Features
* Criar, Alterar e Deletar colaborador 
* Cadastro de colaborador e administrador
* Buscar colaborador por nome

## Rotas Criadas

| Rota                                                                      | Descrição                                 | Métodos Aceitos           | Testada            |
| ------------------------------------------------------------------------- | ----------------------------------------- | ------------------------- | ------------------ |
| [`/colaborador/cadastro`](#cadastra-colaborador)                          | Cadastra colaborador ou admin             | `POST`                    | :white_check_mark: |
| [`/colaboradores `](#pega-todos-colaboradores)                            | Pega todos colaboradores                  | `GET`                     | :white_check_mark: |
| [`/colaborador/detalhes/<int:user_id>` ](#pega-colaborador-específico)    | Pega/Altera/Deleta colaborador específico | `GET, PUT, PATCH, DELETE` | :white_check_mark: |
| [`/colaborador/detalhes/<string:user_name>`](#busca-colaborador-por-nome) | Busca colaborador por nome                | `GET`                     | :white_check_mark: |



## Descrição das Rotas
### **Cadastra colaborador ou admin**

`POST`
```
/colaborador/cadastro
```
``` json
{
	"name":"teste",
	"email":"teste@poli.ufrj.br",
	"password":"1234567890",
	"isAdmin": false
}
```

Resposta:
``` json
200 OK
{
	"email": "teste@poli.ufrj.br",
	"id": 2,
	"name": "teste"
}
```



---------------------------------------------------------




### **Pega todos colaboradores**

`GET`
```
/colaboradores
```
``` json
{

}
```

Resposta:
``` json
200 OK
[
	{
		"email": "fulano@poli.ufrj.br",
		"id": 3,
		"name": "fulano"
	},
	{
		"email": "teste@poli.ufrj.br",
		"id": 2,
		"name": "teste"
	}
]
```



---------------------------------------------------------




### **Pega colaborador específico**

`GET`
```
/colaborador/detalhes/2
```
``` json
{

}
```

Resposta:
``` json
200 OK
{
	"email": "teste@poli.ufrj.br",
	"id": 2,
	"name": "teste"
}
```



---------------------------------------------------------




### **Altera completamente informações de colaborador específico**

`PUT`
```
/colaborador/detalhes/2
```
``` json
{
	"name":"Rosa",
	"email":"teste@poli.ufrj.br",
	"password":"0987654321"
}
```

Resposta:
``` json
200 OK
{
	"email": "teste@poli.ufrj.br",
	"id": 2,
	"name": "Rosa"
}
```



---------------------------------------------------------




### **Altera parcialmente informações de colaborador específico**
`PATCH`
```
/colaborador/detalhes/3
```
``` json
{
	"email":"fulano@poli.ufrj.br",
	"name": "Poze"
}
```

Resposta:
``` json
200 OK
{
	"email": "fulano@poli.ufrj.br",
	"id": 3,
	"name": "Poze"
}
```


---------------------------------------------------------




### **Deleta colaborador específico**

`DELETE`
```
/colaborador/detalhes/2
```
``` json
{

}
```

Resposta:
``` json
200 OK
{
	"msg": "user has been deleted"
}
```



---------------------------------------------------------


### **Busca colaborador por nome**

`GET`
```
/colaborador/detalhes/Poze
```
``` json
{

}
```

Resposta:
``` json
200 OK
{
	"email": "fulano@poli.ufrj.br",
	"id": 3,
	"name": "Poze"
}
```







---------------------------------------------------------






































# Autenticação :closed_lock_with_key:
Cria a autenticação do sistema

## Features
* Login de colaborador e admin
* <u>Esqueci minha senha:</u>	
  1. [`/esquecisenha `](#envia-email-com-pin-de-restauração): Manda e-mail para usuario com pin de troca de senha
  2. [`/pinInserido`](#Recebe-pin-do-usuario-e-verifica-se-é-valido): Retorna se pin inserido é valido ou não 
  3. [`/esquecisenha/novasenha/<int:user_id>` ](#usuario-trocar-de-senha-com-pin-recebido): Recebe nova senha do usuario

## Rotas Criadas

| Rota                                                                                  | Descrição                                        | Métodos Aceitos | Testada            |
| ------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------- | ------------------ |
| [`/login`](#faz-login-de-colaborador-e-admin)                                         | Faz login de colaborador e admin                 | `POST `         | :white_check_mark: |
| [`/pinInserido`](#Recebe-pin-do-usuario-e-verifica-se-é-valido)                       | Recebe pin do usuario e verifica se é valido     | `POST `         | :white_check_mark: |
| [`/esquecisenha `](#envia-email-com-pin-de-restauração)                               | Envia email com pin de restauração               | `POST`          | :white_check_mark: |
| [`/esquecisenha/novasenha/<int:user_id>` ](#usuario-trocar-de-senha-com-pin-recebido) | Usuario trocar de senha com pin recebido         | `PATCH`         | :white_check_mark: |
| [`/refreshToken`](#retorna-novo-token-de-acesso-para-usuario-logado)                  | Retorna novo token de acesso para usuario logado | `GET`           | :white_check_mark: |

## Descrição das Rotas
### **Faz login de colaborador e admin**

`POST`
```
/login
```
``` json
{
	"email":"emanuelaires@poli.ufrj.br",
	"password":"1234567890"
}
```

Resposta:
``` json
200 OK
{
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY0MDgwNCwianRpIjoiZTYxNDMxYzYtZDI2Yy00NGRhLTgyYmMtOGY3ODk2ZWVhNTg4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjU3NjQwODA0LCJleHAiOjE2NTc2NDE3MDQsImlzQWRtaW4iOnRydWV9.ifecPCxLADewTvz7bhbRUgxzFOfU9eaVBcWOp-yJUSI",
	"refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY0MDgwNCwianRpIjoiYmYyNGFjNTYtODU0YS00N2UyLWIwYjAtODY1ZjA5NGI1ZGI4IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjEsIm5iZiI6MTY1NzY0MDgwNCwiZXhwIjoxNjYwMjMyODA0fQ.LDwBmiWRoBRXXeDVdyrFRTbs6C6rzeFTr6Qr5g2id3Y",
	"user": {
		"email": "emanuelaires@poli.ufrj.br"
	},
	"isAdmin": true
}
```



---------------------------------------------------------



### **Recebe pin do usuario e verifica se é valido**

`POST`
```
/pinInserido
```
``` json
{
	"email": "colaborannnnnnnnnnnnnndor@sw-simone.com",
	"verificationPin": 1234567
}
```

Resposta:
``` json
200 OK
{
	"isPinValid": true,
	"id": 2
}
```



---------------------------------------------------------





### **Envia email com pin de restauração**

`POST`
```
/esquecisenha
```
``` json
{
	"email":"emanuelaires@poli.ufrj.br"
}
```

Resposta:
``` json
200 OK
{
	"msg": "email enviado com pin"
}
```



---------------------------------------------------------




### **Usuario trocar de senha com pin recebido**

`PATCH`
```
/esquecisenha/novasenha/<int:user_id>
```
``` json
{
	"password":"foilindao",
}
```

Resposta:
``` json
200 OK
{
	"msg": "senha atualizada"
}
```



---------------------------------------------------------




### **Retorna novo token de acesso para usuario logado**

`GET`
```
/refreshToken
```
``` json
{
	"email":"emanuelaires@poli.ufrj.br",
	"password":"1234567890"
}
```

Resposta:
``` json
200 OK
{
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY0MDgwNCwianRpIjoiZTYxNDMxYzYtZDI2Yy00NGRhLTgyYmMtOGY3ODk2ZWVhNTg4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjU3NjQwODA0LCJleHAiOjE2NTc2NDE3MDQsImlzQWRtaW4iOnRydWV9.ifecPCxLADewTvz7bhbRUgxzFOfU9eaVBcWOp-yJUSI"
}
```
























# Autor :notebook:
Criar autores para arquivo

## Features
* Criar e Deletar autor

## Rotas Criadas

| Rota                                                | Descrição                      | Métodos Aceitos | Testada            |
| --------------------------------------------------- | ------------------------------ | --------------- | ------------------ |
| [`/autor/create `](#criar-autor)                    | Criar autor                    | `POST `         | :white_check_mark: |
| [`/autores `  ](#pegar-todos-autores)               | Pegar todos autores            | `GET`           | :white_check_mark: |
| [`/autor/<int:author_id>`](#pegar-autor-específico) | Pegar/Deletar autor específico | `GET, DELETE`   | :white_check_mark: |

## Descrição das Rotas
### **Criar autor**

`POST`
```
/autor/create
```
``` json
{
	"name":"Albert Einstein"
}
```

Resposta:
``` json
200 OK
{
    "id": 1,
	"name":"Albert Einstein"
}
```



---------------------------------------------------------




### **Pegar todos autores**

`GET`
```
/autores
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
[
	{
		"id": 2,
		"name": "Albert Einstein"
	},
	{
		"id": 1,
		"name": "Stephen Curry"
	}
]
```



---------------------------------------------------------




### **Pegar autor específico**

`GET`
```
/autor/2
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	"id": 2,
	"name": "Stephen Curry"
}
```



---------------------------------------------------------




### **Deletar autor específico**

`DELETE`
```
/autor/2
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	"msg": "author has been deleted"
}
```

# Tag :hash:
Criar tags para arquivo

## Features
* Criar e Deletar tag

## Rotas Criadas

| Rota                                         | Descrição                    | Métodos Aceitos | Testada            |
| -------------------------------------------- | ---------------------------- | --------------- | ------------------ |
| [`/tag/create ` ](#criar-tag)                | Criar tag                    | `POST `         | :white_check_mark: |
| [`/tags `  ](#pegar-todas-tags)              | Pegar todas tags             | `GET`           | :white_check_mark: |
| [`/tag/<int:tag_id>`](#pegar-tag-específica) | Pegar/Deletar tag específica | `GET, DELETE`   | :white_check_mark: |

## Descrição das Rotas
### **Criar tag**

`POST`
```
/tag/create
```
``` json
{
	"name":"Cuidado pessoal"
}
```

Resposta:
``` json
200 OK
{
    "id": 1,
	"name":"Cuidado pessoal"
}
```



---------------------------------------------------------




### **Pegar todas tags**

`GET`
```
/tags
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
[
	{
		"id": 2,
		"name": "Ensino Médio"
	},
	{
		"id": 1,
		"name": "Cuidado pessoal"
	}
]
```



---------------------------------------------------------




### **Pegar tag específica**

`GET`
```
/tag/1
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	"id": 2,
	"name": "Cuidado pessoal"
}
```



---------------------------------------------------------




### **Deletar tag específica**

`DELETE`
```
/tag/2
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	"msg": "tag has been deleted"
}
```

# Arquivo :file_folder:
Criar arquivos e fazer upload de mídias.

## Features
* Criar, Ler, Atualizar e Deletar arquivo.
* Upload, Download e Deletar mídia.

## Rotas Criadas

| Rota                                                             | Descrição                                                      | Métodos Aceitos          | Testada            |
| ---------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------ | ------------------ |
| [`/file `](#criar-arquivo)                                       | Criar/Ler todos arquivos do Banco de Dados                     | `POST `, `GET`           | :white_check_mark: |
| [`/file/<int:file_id> `  ](#ler-arquivo-específico)              | Ler, Atualizar ou Deletar arquivo específico do Banco de Dados | `GET`, `PATCH`, `DELETE` | :white_check_mark: |
| [`/upload_media?media_format=<string:format>`](#upload-de-mídia) | Fazer upload de uma mídia para o Storage                       | `POST`                   | :white_check_mark: |
| [`/media/<int:media_path>`](#download-de-mídia)                  | Pegar ou deletar uma mídia específica do Storage               | `GET`, `DELETE`          | :white_check_mark: |

## Descrição das Rotas
### **Criar arquivo no Banco de Dados**

`POST`
```
/file
```
``` json
{
	"type":"img",
	"click_quantity":0,
	"title":"Titulo do Arquivo",
	"category":"Biologia",
	"area":"Ciências da natureza",
	"year":2021,
	"awarded":"Sim",
	"description":"Descricao do arquivo...",
	"media_path":"c7598a210d164361ab9710a048fa0be0.png",
	"author":[1],
	"tag":[1, 2, 3],
	"creator":1
}
```

Resposta:
``` json
201 CREATED
{
	"area": "Ciências da natureza",
	"authors_associated": [
		{
			"id": 1,
			"name": "Simone"
		}
	],
	"awarded": "Sim",
	"category": "Biologia",
	"click_quantity": 0,
	"creator_id": 1,
	"description": "Descricao do arquivo...",
	"id": 22,
	"media_path": "c7598a210d164361ab9710a048fa0be0.png",
	"tags_associated": [
		{
			"id": 1,
			"name": "Literatura"
		},
		{
			"id": 2,
			"name": "Arte"
		},
		{
			"id": 3,
			"name": "História"
		}
	],
	"title": "Titulo do Arquivo",
	"type": "img",
	"year": 2021
}
```


---------------------------------------------------------

### **Criar arquivo de link no Banco de Dados**

`POST`
```
/file
```
``` json
{
	"type":"link",
	"click_quantity":0,
	"title":"TESTE-EMANUEL-link",
	"category":"sustos de moto",
	"area":"Cazemiru",
	"year":2021,
	"awarded":"Sim",
	"description":"Descricao do arquivo...",
	"media_path":"https://www.youtube.com/watch?v=ThHBdW-zM5U",
	"author":[1],
	"tag":[1, 2, 3],
	"creator":2
}
```

Resposta:
``` json
201 CREATED
{
	"area": "Cazemiru",
	"authors_associated": [
		{
			"id":1,
			"name": "Simone"
		}
	],
	"awarded": "Sim",
	"category": "sustos de moto",
	"click_quantity": 0,
	"creator_id": 2,
	"description": "Descricao do arquivo...",
	"id": 28,
	"media_path": "https://www.youtube.com/watch?v=ThHBdW-zM5U",
	"tags_associated": [
		{
			"id": 1,
			"name": "Literatura"
		},
		{
			"id": 2,
			"name": "Arte"
		},
		{
			"id": 3,
			"name": "História"
		}
	],
	"title": "TESTE-EMANUEL-link",
	"type": "link",
	"year": 2021
}
```

---------------------------------------------------------




### **Ler todos arquivos do Banco de Dados**

`GET`
```
/file
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
[
	{
		"area": "Ciências da natureza",
		"authors_associated": [
		{
			"id": 1,
			"name": "Simone"
		}
		],
		"awarded": "Sim",
		"category": "Biologia",
		"click_quantity": 0,
		"creator_id": 1,
		"description": "Descricao do arquivo...",
		"id": 22,
		"media_path": "c7598a210d164361ab9710a048fa0be0.png",
		"tags_associated": [
		{
			"id": 1,
			"name": "Literatura"
		},
		{
			"id": 2,
			"name": "Arte"
		},
		{
			"id": 3,
			"name": "História"
		}
		],
		"title": "Titulo do Arquivo",
		"type": "img",
		"year": 2021
	},

	{
	"area": "Cazemiru",
	"authors_associated": [
		{
			"id": 1,
			"name": "Simone"
		}
	],
	"awarded": "Sim",
	"category": "sustos de moto",
	"click_quantity": 0,
	"creator_id": 2,
	"description": "Descricao do arquivo...",
	"id": 28,
	"media_path": "https://www.youtube.com/watch?v=ThHBdW-zM5U",
	"tags_associated": [
		{
			"id": 1,
			"name": "Literatura"
		},
		{
			"id": 2,
			"name": "Arte"
		},
		{
			"id": 3,
			"name": "História"
		}
	],
	"title": "TESTE-EMANUEL-link",
	"type": "link",
	"year": 2021
}
]
```



---------------------------------------------------------




### **Ler arquivo específico do Banco de Dados**

`GET`
```
/file/22
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	"area": "Ciências da natureza",
	"authors_associated": [
		{
			"id": 1,
			"name": "Simone"
		}
	],
	"awarded": "Sim",
	"category": "Biologia",
	"click_quantity": 0,
	"creator_id": 1,
	"description": "Descricao do arquivo...",
	"id": 22,
	"media_path": "c7598a210d164361ab9710a048fa0be0.png",
	"tags_associated": [
		{
			"id": 1,
			"name": "Literatura"
		},
		{
			"id": 2,
			"name": "Arte"
		},
		{
			"id": 3,
			"name": "História"
		}
	],
	"title": "Titulo do Arquivo",
	"type": "img",
	"year": 2021
}
```

---------------------------------------------------------




### **Atualizar arquivo específico do Banco de Dados**

`PATCH`
```
/file/22
```
``` json
{
	"title":"Novo titulo do arquivo",
	"description":"Nova descrição do arquivo"
}
```

Resposta:
``` json
200 OK
{
	"area": "Ciências da natureza",
	"authors_associated": [
		{
			"id": 1,
			"name": "Simone"
		}
	],
	"awarded": "Sim",
	"category": "Biologia",
	"click_quantity": 0,
	"creator_id": 1,
	"description": "Nova descrição do arquivo",
	"id": 22,
	"media_path": "c7598a210d164361ab9710a048fa0be0.png",
	"tags_associated": [
		{
			"id": 1,
			"name": "Literatura"
		},
		{
			"id": 2,
			"name": "Arte"
		},
		{
			"id": 3,
			"name": "História"
		}
	],
	"title": "Novo titulo do arquivo",
	"type": "img",
	"year": 2021
}
```

---------------------------------------------------------




### **Deletar arquivo específico do Banco de Dados**

`DELETE `
```
/file/22
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	
}
```

---------------------------------------------------------

### **Upload de mídia para o Storage**

`POST `
```
/upload_media?media_format=png
```
__Multipart form data__
```
media: arquivo_para_upload.png
```

Resposta:
``` json
200 OK
{
	"media_path": "721b4c3defe755d19bb16090d0c85ae4.png"
}
```

---------------------------------------------------------

### **Download de mídia do Storage**

`GET `
```
/media/721b4c3defe755d19bb16090d0c85ae4.png
```

``` json
{

}
```

Resposta:
``` json
200 OK
{
	"URL": "https://nyc3.digitaloceanspaces.com/storage-fluxo/sw-simone/c7598a210d164361ab97dfsfs10a048fa0be0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MM6DTS3N2ZXXJUEXLHOW%2F20220802%2Fnyc%2Fs3%2Faws4_request&X-Amz-Date=20220802T215121Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=a0af103a3797c4c3a5a3522680708cd88cba5d633a777f1f494b70c4a655042e"
}
```

---------------------------------------------------------

### **Deletar mídia específica do Storage**

`DELETE `
```
/media/721b4c3defe755d19bb16090d0c85ae4.png
```

``` json
{

}
```

Resposta:
``` json
200 OK
{

}
```

# Banner :beginner:
Criar banners.

## Features
* Criar, Ler, Atualizar e Deletar banner.

## Rotas Criadas

| Rota                                                   | Descrição                                   | Métodos Aceitos          | Testada            |
| ------------------------------------------------------ | ------------------------------------------- | ------------------------ | ------------------ |
| [`/banner `](#criar-banner)                            | Criar/Ler todos os banners                  | `POST `, `GET`           | :white_check_mark: |
| [`/banner/<int:banner_id> `  ](#ler-banner-específico) | Ler, Atualizar ou Deletar banner específico | `GET`, `PATCH`, `DELETE` | :white_check_mark: |

## Descrição das Rotas
### **Criar banner**

`POST`
```
/banner
```
``` json
{
	"banner_name":"quarto-banner",
	"media_path":"721b4c3defe740d19bb16090d0c85ae4.png"
}
```

Resposta:
``` json
201 CREATED
{
	"banner_name": "quarto-banner",
	"id": 3,
	"media_path": "721b4c3defe740d19bb16090d0c85ae4.png"
}
```

---------------------------------------------------------




### **Ler todos banners**

`GET`
```
/banner
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
[
	{
		"banner_name": "primeiro-banner",
		"id": 1,
		"media_path": "c7598a210d164361ab9710a048fa0be0.png"
	},
	{
		"banner_name": "terceiro-banner",
		"id": 2,
		"media_path": "525352532.png"
	},
	{
		"banner_name": "quarto-banner",
		"id": 3,
		"media_path": "721b4c3defe740d19bb16090d0c85ae4.png"
	}
]
```



---------------------------------------------------------




### **Ler banner específico**

`GET`
```
/banner/3
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	"banner_name": "quarto-banner",
	"id": 3,
	"media_path": "721b4c3defe740d19bb16090d0c85ae4.png"
}
```

---------------------------------------------------------




### **Atualizar banner específico**

`PATCH`
```
/file/3
```
``` json
{
	"banner_name":"terceiro-banner",
	"media_path":"525352532.png"
}
```

Resposta:
``` json
200 OK
{
	"banner_name": "terceiro-banner",
	"id": 3,
	"media_path": "525352532.png"
}
```

---------------------------------------------------------




### **Deletar banner específico**

`DELETE `
```
/file/3
```
``` json
{
	
}
```

Resposta:
``` json
200 OK
{
	
}
```


