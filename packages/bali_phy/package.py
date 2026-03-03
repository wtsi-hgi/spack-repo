# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class BaliPhy(MesonPackage):
    """BAli-Phy is software by Ben Redelings and Marc Suchard that estimates multiple sequence alignments and evolutionary trees from DNA, amino acid, or codon sequences. It uses likelihood-based evolutionary models of substitutions and insertions and deletions to place gaps."""

    homepage = "https://www.bali-phy.org/"
    url = "https://github.com/bredelings/BAli-Phy/archive/refs/tags/3.6.0.tar.gz"

    version("4.0-beta15-ubuntu-24.04", sha256="7bfd97165153fae5bde363945f3944890de51ac902129c5a9fa2abc54eaead56")
    version("4.0-beta15-ubuntu-22.04", sha256="cb0bd8706e3e13c03f392c8971d0ec8e3b493bd29d76e47ac4cb951b88e91985")
    version("4.0-beta15-ubuntu-20.04", sha256="b7d08e89656e67616e00d83d84d7ee7c8d2a32232e44cf1fd8fab85dd217cc2d")
    version("4.0-beta15-mac-intel64", sha256="fc3ad8f44dad51c34b19f97d04a5617fec691d764e5b2940b5876ff06d6a5c6c")
    version("4.0-beta15-mac", sha256="f869af9c46db5482f4a7bfea1e0ebb23d83b934cf80cd936a46c1826212beaf5")
    version("4.0-beta15", sha256="4d1b6f08dee5bb359a13a4e2913129fd1f6e0ddb36350c7f8851f583192b4a94")
    version("4.0-beta14-ubuntu-24.04", sha256="06139cef451fd2e6c6cefc9d0d851f9c87d9e71f88e75214e28c6ae34494ec6d")
    version("4.0-beta14-ubuntu-22.04", sha256="6e8f2b52a8f9e4f8e3bc462f327565053c8ee9a5982caa9c74e7669d35b847e0")
    version("4.0-beta14-ubuntu-20.04", sha256="b104ade396515ed70929efa13ab5c2b7c228bb5024ae5b26afc005806352807f")
    version("4.0-beta14-mac-intel64", sha256="acf08f9bd9351fc2bc6630905eb5c0926286fec89cb7b2c96460a0b2d1c1ebe7")
    version("4.0-beta14-mac", sha256="6816744a1c8aa28dc8f4d653f50d081543b1d1f5f33dea3b304d0049068ae5b0")
    version("4.0-beta14", sha256="b3a55d8e89589d5b46a621b1c9ee5bcbe576b6fb6ea22fe3782d10c9830c66f1")
    version("4.0-beta13-mac-intel64", sha256="18c17a1e240e4bd87779cba0db3abc568bb2e79716afbfbc72b84f439a2f6079")
    version("4.0-beta13-mac", sha256="e2124d6f56ed4a14d7db985b5903271b3c8c950f7c5229c6be0f6da442ca4ea9")
    version("4.0-beta13-jammy", sha256="de5800a9db6b8825ba91a3bc6570cd15950e41f897eacb62f94d4c30e53ed718")
    version("4.0-beta13-focal", sha256="0704bfd8bd5fa944d3d1ebd44a9ded569e60e935dccc4a2a7f59e927c1ac30c1")
    version("4.0-beta13", sha256="52131abf92176b4085a6b6fa645e40d2103b61a37d16d4b22eab17f635fb96fe")
    version("4.0-beta11-mac-intel64", sha256="6af74123d954589a8764c546c7cb82ec037024d0a9c352d7a7fc04bf915c6818")
    version("4.0-beta11-mac", sha256="a8cf5ac9711ae49162da5138006b53c10a7ac23843c4ae5fb7913cfb19fa0f17")
    version("4.0-beta11-jammy", sha256="a084a2aaa8fdb1b5bf51f4605cbdbb610749e72c536c5185f98290fe515a4e98")
    version("4.0-beta11-focal", sha256="c06247ebf03469f6decf9d6b26901eaf609bb60088a49330c3bfbca32e3d1ffd")
    version("4.0-beta11", sha256="d73e833fd491df0891746963991ed16b0e0872a0fc9f9b16dc736000c46e3b07")
    version("4.0-beta10-mac-intel64", sha256="2a37d4ad042a20b7bbe1d1c8f958a894f5a6b630ddf34242e965aac22a8fc069")
    version("4.0-beta10-mac", sha256="99e06c5c14398b42686d29b780cabb7eb15baa2a32cb11627fa3941ed7741277")
    version("4.0-beta10", sha256="f936edda2797e30d16b9a31c68e0a31831e5c9baefc99820c5383a2a11e6ad81")
    version("4.0-beta9-mac-intel64", sha256="d4746dafae08bbe23b7cba1f9a2ac4f16db0f226ed78c7aabdfc956fc4713a1d")
    version("4.0-beta9-mac", sha256="0ba3b466c243911a83f4461e7ef5551606b70ec9d402c4e027be57b824b4f38d")
    version("4.0-beta9", sha256="6ae4105151a834497ab89e72fe40eb0712dd55734c332e17caec0e6ea0d8a991")
    version("4.0-beta8-mac64", sha256="6d84aed3fc02f3929b331b2b90d8fe6aa0ac9e6b85e80c3e841bd8dc05687701")
    version("4.0-beta8", sha256="ebeb4c94d41af31c204ea36f5829e81a7bb8b8a4599434e80c630658950c8de2")
    version("4.0-beta7-mac64", sha256="464acdbfc0aba37fd5f0afae081dbf12de15ffd79421205ebd46e9ee0caf8168")
    version("4.0-beta7", sha256="4d39f04f6400ffecc3683ac75f65119549439c92aca07e4037d67bd4a4b973d8")
    version("4.0-beta6-mac64", sha256="e2f0e207e5405f5d97f7d020a433e05b2277d575d082f16cd1fc7f96cf4f99c3")
    version("4.0-beta6", sha256="ee330c68a6f7894df7497c781c71a19f7bf136ab385e47b9b3851a85f75858ac")
    version("4.0-beta5-mac64", sha256="1ee2b7ae9bcbe3922d39740b01d025164776d959e60050d5b32502c8474b3267")
    version("4.0-beta5", sha256="62b01ded448cb9db649e27194eb02aa8e8f7084dec39721ef9afede501765673")
    version("3.6.0", sha256="88f1922f80d0376ec2a0929d72d69258eac3dfba0eef13aab3f9c460db1ac0b6", preferred=True)

    # depends_on("foo")

#    def install(self, spec, prefix):
#        # FIXME: Unknown build system
#        make()
#        make("install")
