import json


def test_sorted():

    with open('../numeros_nao_ordenados.json', 'r') as file:
        unordered_list = json.load(file)

    with open('../numeros_ordenados.json', 'r') as file:
        sorted_list = json.load(file)

    sorted_list_function = sorted(unordered_list)

    assert sorted_list_function == sorted_list
