try:
    import requests
    import pandas as pd
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import PIL
    from PIL import Image

except:
    print('please install libraries using:')
    print('pip install -r requirements.txt')
    exit(1)


import pprint


def test_requests():
    print('testing requests')
    print('version', requests.__version__)
    query1 = 'urban university'
    query2 = query1.replace(' ', '%20')
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    response = requests.get('https://google.com/search', headers=headers, params={'q': query1})
    response.raise_for_status()
    t = response.text.split(f'data-async-context="query:{query2}"')[1].split('bottomads')[0].split('href="')
    for i, r in enumerate(t):
        print(i, r.split('"')[0])


def test_pandas():
    print('testing pandas')
    print('version', pd.__version__)
    mydataset = {
      'cars': ["BMW", "Volvo", "Ford"],
      'passings': [3, 7, 2]
    }
    myvar = pd.DataFrame(mydataset)
    print(myvar)


def test_numpy():
    print('testing numpy')
    print('version', np.__version__)
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)


def test_matplotlib():
    print('testing matplotlib')
    print('version', matplotlib.__version__)
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()


def test_pillow():
    print('testing pillow')
    print('version', PIL.__version__)
    image = Image.new('RGB', (100, 100), (255,0,0))
    image.show()


if __name__ == '__main__':
    test_requests()
    test_pandas()
    test_numpy()
    test_matplotlib()
    test_pillow()
