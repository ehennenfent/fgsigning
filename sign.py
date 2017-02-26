import cbor2
import cv2

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

with open("hack.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

signatures = []
pad = padding.PKCS1v15()
hashtype = hashes.SHA256()

cap = cv2.VideoCapture("./micdrop.mp4")
index = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    signer = private_key.signer(pad, hashtype)
    signer.update(bytes(frame))
    signatures.append([index, signer.finalize(), 0])

    index += 1

cert = open('hack.cer', 'r').read()
signatures.append([0, cert])

cbor_dat = cbor2.dumps(signatures)
with open('signatures.cbor', 'wb') as fp:
    fp.write(cbor_dat)
