from PIL import Image
from tqdm import tqdm

import argparse
import json
from pathlib import Path
import glob

from spritesheetSplit import OG_SPRITE_SIZE, create_sprites


def _get_sprite_data(data: dict) -> list:
    """
    Returns an array containing the sprite ID to use for each block.
    """
    return data["layers"][0]["data"]


def _get_cave_size(data: dict) -> (int, int):
    width = data["layers"][0]["width"]
    height = data["layers"][0]["height"]
    return (width, height)


def read_map_data(pack: int) -> dict:
    file = Path("map_data") / f"{pack}.json"
    with open(file) as f:
        data = json.load(f)
    return data


def load_sprite_images() -> dict:
    images = {}
    for file in Path("cavesprites").glob("*.png"):
        images[file.stem] = Image.open(file)
    return images

def create_properly_sized_sprites(size: int) -> None:
    create_sprites(size)


def create_map(pack: int) -> None:
    print(f"Generating map for pack {pack}...")
    data = read_map_data(pack)
    width, height = _get_cave_size(data)
    max_sprite_size = 55_000 // width
    img_wid = width * max_sprite_size
    img_hei = height * max_sprite_size
    sprite_data = _get_sprite_data(data)
    del data
    create_properly_sized_sprites(max_sprite_size)
    images = load_sprite_images()
    # Instantiate full map size
    print(f"instantiating image ({img_wid}, {img_hei})")
    new_im = Image.new("RGBA", (img_wid, img_hei))
    for row in tqdm(range(0, width)):
        for col in range(0, height):
            loc = row * height + col
            # sprite ID is off by one
            sprite = sprite_data[loc] - 1
            small_img = images[f"{sprite}"]
            new_im.paste(small_img, ((col * max_sprite_size), (row * max_sprite_size)))
    print(f"Saving image for pack {pack}. This will take some time.")
    new_im.save(Path('full_maps') / f"map_{pack}.png")
    print("saved")
    del new_im


if __name__ == "__main__":
    packs = [
         1026,
         10930,
         11833,
         12890,
         2773,
         4775,
         6294,
         10540,
         11072,
         12641,
         1701,
         4418,
         5047,
         993,
    ]
    parser = argparse.ArgumentParser(description="Generate full map for a pack's cave.")
    parser.add_argument("pack", help="enter the pack ID", type=int, choices=packs)
    args = parser.parse_args()
    create_map(args.pack)
