rows = int(input())


def first_half(rows_count):
    for row in range(1, rows_count + 1):
        result = f"{' '*(rows_count - row)}{'* ' * row}"
        print(result[:-1])


def second_half(rows_count):
    for row in range(1, rows_count):
        result = f"{' ' * row}{'* '* (rows_count - row)}"
        print(result[:-1])


def print_rhombus(rows_count):
    first_half(rows_count)
    second_half(rows_count)


print_rhombus(rows)
