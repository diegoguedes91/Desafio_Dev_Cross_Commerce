import requests
import json


def extract_api(counter=1):
    disordered_list = []
    while True:
        request = requests.get(
            f"http://challenge.dienekes.com.br/api/numbers?page={counter}"
        )
        extract = request.json()

        if extract == {"numbers": []}:
            break

        if extract == {"error": "Simulated internal error"}:
            while extract == {"error": "Simulated internal error"}:
                request = requests.get(
                    f"http://challenge.dienekes.com.br/api/numbers?page={counter}"
                )
                extract = request.json()
            disordered_list.extend(extract["numbers"])
        else:
            disordered_list.extend(extract["numbers"])
        counter += 1

    with open("numeros_nao_ordenados.json", "w") as files:
        json.dump(disordered_list, files)

    return disordered_list


def transform_api():
    def merge_sort(sorted_list):

        if len(sorted_list) <= 1:
            return sorted_list
        mid = len(sorted_list) // 2

        list_left, list_right = merge_sort(sorted_list[:mid]), merge_sort(
            sorted_list[mid:]
        )

        return merge(list_left, list_right, sorted_list.copy())

    def merge(list_left, list_right, merged):

        left_cursor, right_cursor = 0, 0
        while left_cursor < len(list_left) and right_cursor < len(list_right):

            if list_left[left_cursor] <= list_right[right_cursor]:
                merged[left_cursor + right_cursor] = list_left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = list_right[right_cursor]
                right_cursor += 1

        for left_cursor in range(left_cursor, len(list_left)):
            merged[left_cursor + right_cursor] = list_left[left_cursor]

        for right_cursor in range(right_cursor, len(list_right)):
            merged[left_cursor + right_cursor] = list_right[right_cursor]

        return merged

    sorted_list = extract_api()

    sorted_list = merge_sort(sorted_list)

    with open("numeros_ordenados.json", "w") as files:
        json.dump(sorted_list, files)


def load():

    with open("numeros_ordenados.json", "r") as files:
        sorted_list = json.load(files)

    return str(sorted_list)
