import json
import timeit
import requests


def get_movie_detail(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=95e98be9732737c7176da31270ca6807"
    response = requests.get(url)

    return response.json()


if __name__ == "__main__":
    result = []
    ROWS = 1000

    with open('./data.json', 'r') as datafile:
        data = json.load(datafile)

    starttime = timeit.default_timer()
    for mid in data[:ROWS]:
        movie_detail = get_movie_detail(mid)
        result.append(movie_detail)
    print("The time taken is :", timeit.default_timer() - starttime)
    print(len(result))
