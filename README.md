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

## Motivation

Video and audio creation technology gets better every day. Within a few years, it'll likely be possible for a user with relatively little expertise and standard desktop hardware to create nearly-undetectable forged video and audio of people without their consent. With such power in the hands of so many, how can we avoid entering a post-truth society, where one cannot believe anything one did not witness with one's eyes and ears?

We can't solve this problem entirely, but we think this project might be a step in the right direction. Asymmetric cryptography allows us to validate a file to verify that it was signed, in its exact binary form, by the holder of a unique private key. Want to prove that your footage of a real-estate tycoon hanging out in Moscow is legit? In the future, your camera could sign the footage with a hardware-backed private key, and by demonstrating that the signatures from the camera were still intact, you could prove that your footage wasn't fabricated with advanced CGI.

Admittedly, cryptographic signing isn't a new technique, for video files, it makes a lot more sense to sign blocks of data with much smaller granularity than the entire file. With a bit more work (and of course, widespread community acceptance) this project could allow media creators to prove the validity of their video without losing all ability to edit it.

## Contributor Guide
[To-do list](https://github.com/ehennenfent/fgsigning/blob/master/CONTRIBUTING.md)

## License
Currently GNU Lesser GPL. Likely switching to an MIT license within the next six months.
