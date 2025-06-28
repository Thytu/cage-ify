import os
import requests

from tqdm import tqdm
from duckduckgo_search import DDGS


START_SUFFIX = "_start.jpg"
END_SUFFIX = "_end.jpg"



def download_cage_images(output_dir: str, query: str = "Nicolas Cage", max_results: int = 100):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with DDGS() as ddgs:
        results = ddgs.images(
            keywords=query,
            region="wt-wt",
            safesearch="moderate",
            size="Large",
            type_image="photo",
            max_results=max_results
        )

        for i, result in tqdm(enumerate(results), total=max_results):
            try:
                img_url = result['image']
                response = requests.get(img_url, timeout=10)

                if response.status_code == 200:
                    filename = f"{output_dir}/{i:03d}{END_SUFFIX}"
                    with open(filename, 'wb') as f:
                        f.write(response.content)

            except Exception as e:
                print(f"Error downloading image {i}: {e}")


if __name__ == "__main__":
    download_cage_images(output_dir="dataset")
