import json
import time
import timeit
import requests
import threading


def get_movie_detail(movie_id: int, result: list):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=95e98be9732737c7176da31270ca6807"
    response = requests.get(url)

    result.append(response.json())


def threaded_activity(activity_list, activity_func, result, n_threads):
    threads = list()
    index = 0

    while True:
        thread_count = threading.active_count()
        if thread_count <= n_threads and index < len(activity_list):
            x = threading.Thread(target=activity_func, args=(
                activity_list[index], result))
            x.start()
            index += 1

        if thread_count == 1 and index == len(activity_list):
            break

        time.sleep(0.001)


if __name__ == "__main__":
    result = []
    ROWS = 1000
    N_THREADS = 8

    with open('./data.json', 'r') as datafile:
        data = json.load(datafile)

    starttime = timeit.default_timer()
    threaded_activity(data[:ROWS], get_movie_detail, result, N_THREADS)
    print("The time taken is :", timeit.default_timer() - starttime)

    print(len(result))
