from PIL import Image


OG_SPRITE_SIZE = 66


def create_sprites(size: int) -> None:
    sheet = Image.open("cavesprites.png")
    count = 0
    # sprite sheet has 4 rows and 16 cols
    for y in range(4):
        for x in range(16):
            a = (x + 1) * OG_SPRITE_SIZE
            b = (y + 1) * OG_SPRITE_SIZE
            sprite = sheet.crop((a - OG_SPRITE_SIZE, b - OG_SPRITE_SIZE, a, b))
            sprite = sprite.resize((size, size))
            sprite.save(f"cavesprites/{count}.png")
            count += 1
