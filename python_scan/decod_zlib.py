import zlib

with open("zlib_payload.bin", "rb") as f:
    data = f.read()

try:
    decompressed = zlib.decompress(data)
    with open("decompressed_output.bin", "wb") as out:
        out.write(decompressed)
    print("[+] Décompression réussie. Fichier écrit dans 'decompressed_output.bin'")
except Exception as e:
    print(f"[!] Erreur : {e}")
