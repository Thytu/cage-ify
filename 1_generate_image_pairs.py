import os
import random
import asyncio
import requests
import fal_client

from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()


PROMPTS = [
    "Replace Nicolas Cage's face with Ryan Reynolds' face",
    "Replace Nicolas Cage's face with Tom Hanks' face",
    "Replace Nicolas Cage's face with Brad Pitt's face",
    "Replace Nicolas Cage's face with Johnny Depp's face",
    "Replace Nicolas Cage's face with Leonardo DiCaprio's face",
]

START_SUFFIX = "_start.jpg"
END_SUFFIX = "_end.jpg"


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

        if file.endswith(END_SUFFIX) and not os.path.exists(f"dataset/{file.replace(END_SUFFIX, START_SUFFIX)}"):
            tasks.append(generate_image_pair(random.choice(PROMPTS), f"dataset/{file}", f"dataset/{file.replace(END_SUFFIX, START_SUFFIX)}"))

    for i in tqdm(range(0, len(tasks), batch_size)):
        await asyncio.gather(*tasks[i:min(i + batch_size, len(tasks))])


if __name__ == "__main__":
    asyncio.run(main())
