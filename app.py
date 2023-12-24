from flask import Flask, render_template, request
import copy

app = Flask(__name__)

# Sorting Algorithms


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Routes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sort', methods=['POST'])
def sort():
    numbers = request.form['numbers']
    numbers = [int(x) for x in numbers.split(" ")]
    algorithm_choice = request.form['algorithm']

    if algorithm_choice == 'insertion':
        sorted_numbers = insertion_sort(copy.deepcopy(numbers))
        algorithm_used = 'Insertion Sort'
    elif algorithm_choice == 'merge':
        sorted_numbers = merge_sort(copy.deepcopy(numbers))
        algorithm_used = 'Merge Sort'
    elif algorithm_choice == 'bubble':
        sorted_numbers = bubble_sort(copy.deepcopy(numbers))
        algorithm_used = 'Bubble Sort'
    else:
        return "Invalid choice"

    numbers_str = ', '.join(str(num) for num in numbers)

    sorted_numbers_str = ', '.join(str(num) for num in sorted_numbers)

    return render_template('result.html', algorithm_used=algorithm_used, numbers=numbers_str, sorted_numbers=sorted_numbers_str)


if __name__ == '__main__':
    app.run(debug=True)


