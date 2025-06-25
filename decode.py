from PIL import Image

def to_text(binary_data):
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def decode_lsb(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            binary_data += str(pixel[0] & 1)
    # Split into 8-bit chunks and convert to text
    decoded_text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        char = chr(int(byte, 2))
        decoded_text += char
        if decoded_text.endswith("|||END|||"):
            return decoded_text[:-8]  # Remove the delimiter
    return "No hidden message found."

if __name__ == "__main__":
    print("=== LSB Steganography Decoder ===")
    in_img = input("Input image path: ").strip()
    message = decode_lsb(in_img)
    print("Hidden message:", message)