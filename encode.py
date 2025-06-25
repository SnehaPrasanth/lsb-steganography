from PIL import Image

def to_bin(data):
    """Convert string to binary."""
    return ''.join([format(ord(i), '08b') for i in data])

def encode_lsb(image_path, output_path, secret_text):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    secret_text += "|||END|||"
    binary_secret = to_bin(secret_text)
    data_len = len(binary_secret)
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < data_len:
                pixel = list(img.getpixel((x, y)))
                # Modify only the red channel's LSB
                pixel[0] = (pixel[0] & ~1) | int(binary_secret[idx])
                encoded.putpixel((x, y), tuple(pixel))
                idx += 1
            else:
                encoded.save(output_path)
                print(f"Text hidden in {output_path}")
                return
    print("Warning: Text too long for this image!")

if __name__ == "__main__":
    print("=== LSB Steganography Encoder ===")
    in_img = input("Input image path: ").strip()
    out_img = input("Output image path: ").strip()
    secret = input("Text to hide: ")
    encode_lsb(in_img, out_img, secret)