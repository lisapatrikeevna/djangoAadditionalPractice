# Schreiben Sie eine Funktion, die drei Wörter
# als Eingabe erhält und bestimmt, ob sie Anagramme
# voneinander sind. Verwenden Sie Mengen.
# Die Funktion gibt true zurück, wenn die Wörter Anagramme sind,
# und false im anderen Fall. Beispiel:
# anagram("кластер", "стрелка", "сталкер") = true.

def anagramm(w1, w2, w3):
    arr1 = set(w1)
    arr2 = set(w2)
    arr3 = set(w3)

    return arr1 == arr2 == arr3



print(anagramm('кластер', 'стрелка', 'сталкер'))


from collections import defaultdict


def sales_product_data(sales_data):
    customer_data = defaultdict(lambda: defaultdict(int))

    for sales in sales_data:
        client_name, item, quantity = sales.split('')
        quantity = int(quantity)
        customer_data[client_name][item] += quantity

    sales_data = [
        "Bob Birne 3",
        "Alice Birne 1",
        "Bob Apfel 1",
        "Charlie Apfel 5",
        "Alice Apfel 3",
        "Charlie Birne 2"
    ]



    for client_name in sorted(customer_data):
        print(f'All clients {customer_data: client_name, item, quantity} {client_name}')
