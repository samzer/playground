import json
import timeit
import requests
import threading


def get_movie_detail(movie_id: int, result: list):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=95e98be9732737c7176da31270ca6807"
    response = requests.get(url)

    result.append(response.json())


def threaded_activity(activity_list, activity_func, result):
    threads = list()

    # start the threads
    for i in activity_list:
        x = threading.Thread(target=activity_func, args=(i, result))
        threads.append(x)
        x.start()

    # Wait for the threads to finish
    for index, thread in enumerate(threads):
        thread.join()


if __name__ == "__main__":
    result = []
    ROWS = 1000
    N_THREADS = 8

    with open('./data.json', 'r') as datafile:
        data = json.load(datafile)

    starttime = timeit.default_timer()

    mdata = data[:ROWS]
    for i in range(0, len(mdata), N_THREADS):
        threaded_activity(mdata[i: i + N_THREADS], get_movie_detail, result)
    print("The time taken is :", timeit.default_timer() - starttime)
    print(len(result))
