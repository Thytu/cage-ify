import os
import asyncio
import requests
import fal_client

from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()


PROMPT = "Replace Nicolas Cage's face with Ryan Reynolds' face"


async def generate_image_pair(prompt: str, image_path: str, output_path: str):

    url = fal_client.upload_file(image_path)

    handler = await fal_client.submit_async(
        "fal-ai/flux-pro/kontext/max",
        arguments={
            "prompt": prompt,
            "image_url": url,
        },
    )

    request_id = handler.request_id

    result = await fal_client.result_async("fal-ai/flux-pro/kontext/max", request_id)

    response = requests.get(result["images"][0]["url"])

    with open(output_path, "wb") as f:
        f.write(response.content)

    return


async def main(batch_size: int = 10):

    tasks = []

    for file in os.listdir("dataset"):

        if file.endswith("_start.jpg") and not os.path.exists(f"dataset/{file.replace('_start.jpg', '_end.jpg')}"):
            tasks.append(generate_image_pair(PROMPT, f"dataset/{file}", f"dataset/{file.replace('_start.jpg', '_end.jpg')}"))

    for i in tqdm(range(0, len(tasks), batch_size)):
        await asyncio.gather(*tasks[i:min(i + batch_size, len(tasks))])


if __name__ == "__main__":
    asyncio.run(main())
