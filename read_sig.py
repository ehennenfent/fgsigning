import cbor2, cv2, binascii
import pem
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
import pprint as pp

signatures = []
certificates = []
with open('signatures.cbor', 'rb') as fp:
    cbor_import = cbor2.load(fp)

    cert = cbor_import[-1]
    signatures = cbor_import[:-(1 + cbor_import[-1][0])]
    for i in range(cert[0] + 1):
        certificates.append(cbor_import[-(i + 1)][1])

if(len(certificates) > 1):
    print("Warning: Multiple certificates not currently supported")

certificate = certificates[0]

certs = pem.parse(bytes(certificate.encode('utf-8')))
cert = x509.load_pem_x509_certificate(bytes(str(certs[0]).encode('utf-8')), default_backend())
pubkey = cert.public_key()
pad = padding.PKCS1v15()
hashtype = hashes.SHA256()

cap = cv2.VideoCapture("./micdrop.mp4")
index = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if(signatures[index][0] != index):
        print("Error: Frame index mismatch")
        continue

    try:
        pubkey.verify(signatures[index][1], bytes(frame), pad, hashtype)
        print("Frame {0} OK <{1}>".format(index, binascii.hexlify(signatures[index][1][:4]).decode('utf-8')))
    except InvalidSignature:
        print("BAD SIGNATURE on frame %s" % index)

    index += 1

print("Frames 0-{0} were signed by the following certificate <{1}>:".format(index, binascii.hexlify(cert.fingerprint(hashtype)).decode('utf-8')))
pp.pprint(cert.subject.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME))
pp.pprint(cert.subject.get_attributes_for_oid(x509.NameOID.STATE_OR_PROVINCE_NAME))
pp.pprint(cert.subject.get_attributes_for_oid(x509.NameOID.LOCALITY_NAME))
pp.pprint(cert.subject.get_attributes_for_oid(x509.NameOID.ORGANIZATION_NAME))
pp.pprint(cert.subject.get_attributes_for_oid(x509.NameOID.ORGANIZATIONAL_UNIT_NAME))
pp.pprint(cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME))
