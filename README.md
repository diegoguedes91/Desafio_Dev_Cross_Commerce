# Desafio_Dev_Cross_Commerce
Repositório para o desafio Dev Cross Commerce


## Requisitos: 

git clone https://github.com/diegoguedes91/Desafio_Dev_Cross_Commerce.git

Flask  - versão 2.0.2
```python
pip install flask
```
Requests
```python
pip install requests 
```
Pytest - versão 6.2.5
```python
pip install pytests
```
Black - versão 21.12b0
```python
pip install black 
```

## Rota para acessar a API:

Segue abaixo a rota para vizualizar os numeros de forma ordenada: 

http://127.0.0.1:5000/numbers 
![API](https://github.com/diegoguedes91/Desafio_Dev_Cross_Commerce/blob/main/output_sorted_list.png)

## Etapas: 

Todas as estapas(Extract, Transform, e Load) estão localizadas no modulo __commits__ 

### 1. Extract

Na etapa extract é feito a chamada na página e adicionado as informações em uma lista. Caso retorne o erro "Simulated internal error" é feito uma nova requisição a mesma pagina até retornar com o resultado esperado, conforme o exemplo abaixo: 
```python 
if extract == {"error": "Simulated internal error"}:
            while extract == {"error": "Simulated internal error"}:
                request = requests.get(
                    f"http://challenge.dienekes.com.br/api/numbers?page={counter}"
                )
```
Esta etapa só é concluída quando API retorna o valor _{"numbers": []}:_. Ao final a função extract salva os valores em um arquivo .json e retorna uma lista desordenada. 

### 2. Transform

A função _transform_api_ é baseada no algoritmo Merge Sort, no qual divide em sublistas, faz a ordenação e mescla novamente. A função recebe a lista desordenada de _extract_api_, faz toda a ordenação e salva uma lista toda ordenada em um arquivo .json.

### 3. load 

A função _load_ abre o arquivo .json de lista ordenadas  e salva em uma lista convertida em string para subir na aplicação no Flask. 

## Main 

O modulo _main_ utiliza o Flask para subir a API. Conforme a etapa _load_, a API utiliza as informações salvas no arquivo de numeros ordenados .json, para que sempre este arquivo esteja atualizado foi inserido uma _trhead_ que faz chamada na função _transform_api_ no qual faz a chamada para as requisições novamente e faz a transformação de dados, deixando sempre o arquivo .json atualizado.

```python
def update():
    while True:
        transform_api()
        time.sleep(60)


server = Flask(__name__)


@server.get("/numbers")
def upload_list():
    return load()


if __name__ == "__main__":
    threading.Thread(target=update).start()
    server.run()
```

## Teste

O teste executado garante que a etapa transform esteja resultando dados integros, provando que o algoritmo esta retornando informações realmente ordenadas. 
Conforme o codigo abaixo é utilizado em uma variavel o arquivo .json de numeros não ordenados gerados pela etapa *extract* e outra variavel recebendo outro arquivo .json de numeros ja ordenados feito pela etapa *transform*. 
A variavel que recebe numeros não ordenados passa pela função do python _sorted_ na qual ordena os numeros automaticamente, o teste faz a comparação com os numeros ordenados pelo *transform* com os numeros gerados pela função *sorted*.

```python
import json


def test_sorted():

    with open('../numeros_nao_ordenados.json', 'r') as file:
        unordered_list = json.load(file)

    with open('../numeros_ordenados.json', 'r') as file:
        sorted_list = json.load(file)

    sorted_list_function = sorted(unordered_list)

    assert sorted_list_function == sorted_list
```
O teste foi executado com sucesso pelo Pytest. 

![pytest](https://github.com/diegoguedes91/Desafio_Dev_Cross_Commerce/blob/main/tests/sorted_test.png)

