import requests

def test_steam_reviews(app_id):
    url = f"https://store.steampowered.com/appreviews/{app_id}"
    
    params = {
        'json': 1,
        'filter': 'recent',
        'language': 'polish',
        'cursor': '*',
        'num_per_page': 5 
    }
    
    print(f"Downloading {params['num_per_page']} reviews from Steam API for game ID: {app_id}...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print('='*50)
        print('Response:')
        print(data)
        print('='*50)
        if data.get('success') == 1:
            print(f"Downloaded reviews: {len(data['reviews'])}")
            
            if data['reviews']:
                first_review = data['reviews'][0]
                print(f"First review: {first_review['review']}")
                print(f"Recommended? {first_review['voted_up']}")
            else:
                print("No reviews found.")
        else:
            print("HTTP ok, but received internal Steam Error.")
    else:
        print(f"HTTP Error: {response.status_code}")

if __name__ == "__main__":
    # AppID 292030 = The Witcher 3: Wild Hunt
    test_steam_reviews(292030)