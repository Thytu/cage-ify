import os
import zipfile
import asyncio
import fal_client

from dotenv import load_dotenv


load_dotenv()


DATASET_PATH = "dataset"
ZIP_NAME = "dataset.zip"
PROMPTS = "Replace the face with Nicolas Cage's face"


def create_zip(path_to_dataset: str):
    with zipfile.ZipFile(ZIP_NAME, "w") as zipf:
        for file in os.listdir(path_to_dataset):
            zipf.write(os.path.join(path_to_dataset, file), file)


async def trigger_training(path_to_zip: str, default_caption: str):

    url = fal_client.upload_file(path_to_zip)

    handler = fal_client.submit_async(
        "fal-ai/flux-kontext-trainer",
        arguments={
            "image_data_url": url,
            "steps": 1000,
            "learning_rate": 0.0001,
            "default_caption": default_caption,
        },
    )

    request_id = handler.request_id

    print(f"Triggered training, request_id: {request_id}. To check status, go to https://fal.ai/models/fal-ai/flux-kontext-trainer/requests")


async def main():

    if os.path.exists(ZIP_NAME):
        os.remove(ZIP_NAME)

    create_zip(path_to_dataset=DATASET_PATH)

    await trigger_training(ZIP_NAME, PROMPTS)


if __name__ == "__main__":
    asyncio.run(main())
