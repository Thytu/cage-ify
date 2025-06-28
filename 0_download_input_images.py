import os
import requests

from duckduckgo_search import DDGS


def download_cage_images(output_dir: str, query: str = "Nicolas Cage", max_results: int = 100):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with DDGS() as ddgs:
        results = ddgs.images(
            keywords=query,
            region="wt-wt",
            safesearch="moderate",
            size="medium",
            max_results=max_results
        )

        for i, result in enumerate(results):
            try:
                img_url = result['image']
                response = requests.get(img_url, timeout=10)

                if response.status_code == 200:
                    filename = f"{output_dir}/{i:03d}_start.jpg"
                    with open(filename, 'wb') as f:
                        f.write(response.content)

            except Exception as e:
                print(f"Error downloading image {i}: {e}")


if __name__ == "__main__":
    download_cage_images(output_dir="dataset")
