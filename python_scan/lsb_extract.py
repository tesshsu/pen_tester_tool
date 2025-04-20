from PIL import Image
import base64

# Load image
img = Image.open("Mon_Document.png")
pixels = img.load()
width, height = img.size
bits = ""

# Extract LSB from RGB channels
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        bits += str(r & 1)  # LSB of red
        bits += str(g & 1)  # LSB of green
        bits += str(b & 1)  # LSB of blue

# Convert bits to ASCII
text = ""
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) == 8:
        char = chr(int(byte, 2))
        if char.isprintable():
            text += char

print("Extracted text:", text)

# Check for Data URL
if "data:" in text:
    print("Found Data URL:", text)
    if "base64," in text:
        b64_part = text.split("base64,")[1].rstrip("=").strip()
        try:
            decoded = base64.b64decode(b64_part).decode()
            print("Decoded Data URL:", decoded)
        except Exception as e:
            print("Base64 decoding failed:", e)
else:
    print("No Data URL found in LSB")