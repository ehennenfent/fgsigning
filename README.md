# Fighting Fake News with Crypto

Fine-Grained Video Authenticity Certification via RSA Signatures
    * Writes a backing cbor file containing frame-by-frame signatures for a video, then validates these signatures

## USAGE
  `python sign.py`

  `python read_sig.py`


## OUTPUT

    Frames 0-51 were signed by the following certificate <30d517ecdaf49a60339c2e41cb255059dfa0ef350baebea26dfc73b2d1b987dc>:
    [<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.6, name=countryName)>, value='US')>]
    [<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.8, name=stateOrProvinceName)>, value='Illinois')>]
    [<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.7, name=localityName)>, value='Urbana')>]
    [<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.10, name=organizationName)>, value='HackIllinois')>]
    [<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.11, name=organizationalUnitName)>, value='Eric Hennenfent')>]
    [<NameAttribute(oid=<ObjectIdentifier(oid=2.5.4.3, name=commonName)>, value='Fine-Grained Video Signing Key')>]

## OTHER SOURCES OF DOCUMENTATION

## Contributor Guide
[LINK TO CONTRIBUTING.md]

## License
