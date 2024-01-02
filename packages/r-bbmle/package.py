# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbmle(RPackage):
    """Methods and functions for fitting maximum likelihood models in R. This package modifies and extends the 'mle' classes in the 'stats4' package."""

    #url = "https://cran.r-project.org/src/contrib/bbmle_1.0.25.tar.gz"
    cran = "bbmle"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("1.0.25", sha256="86a8c69902fbf6caf337f9bc532afe89dc2a59dd24287a2423d781797010b255")
    version("1.0.24", sha256="01edc00479fabf7491e47ff59bc4adbe6f0d4c23d22e76d1d49c4c1b6b4693ad")
    version("1.0.23.1", sha256="60421eb01190b741ab14885eaf1088f51d49dcf70e58c42b360489bca04e745c")
    version("1.0.22", sha256="84f27690ceadee62cac28ed3ae0fe0365a1b7d479cfbe641263c0e577829b6c5")
    version("1.0.20", sha256="6c0fe8df7243f8a039e62d14014065df2002b9329c0e8a3c2df4e7ccf591f1f7")
    version("1.0.19", sha256="e882d7401126ae1a965e5e8d612c12441f45e9f10d9d2b3453643f1378359004")
    version("1.0.18", sha256="b237c30ccdb0fd6dd835c16270c85afd9165a7d81500908189f678abab09923d")
    version("1.0.17", sha256="53656d23af17b808f3163dbe83d10349cb00f19cdca95a017320026be9137dc8")
    version("1.0.16", sha256="ea2589270a342a741bc238784a7f33e45e64506db7f6423a825d54d46a726e8c")
    version("1.0.15", sha256="43540b741dd4354bf8695f3906c0370a070d548c0685719acb73fa708395042b")
    version("1.0.13", sha256="c64297abf5f5f112dc7c80f34952e702a99fb8aa9204c2823b06bb8b7d3550cf")
    version("1.0.11", sha256="7e5b76fbe6dd5bc0d1870e028e624c0557e1ebbe87e2dbdb4cb7529417f45d0c")
    version("1.0.5.2", sha256="43c10bd03692773ef8065e8c0a45a6d436fbdb4c6eee9bdb5ffff12d8880a591")
    version("1.0.5.1", sha256="f6175a63fd15495f6a3494e55d79885da01e7bb9d0ac015732b7f8a8b35d63bf")
    version("1.0.4.1", sha256="fca5333454476fbe8dfcd2c3a24add8b10c2eca07958b60cc53c90b721e85d25")
    version("1.0.4", sha256="de3ff1b72edc021a94850fd209bef0983acc1eb8e80834c53a6a99d7d7fdc40b")
    version("1.0.3", sha256="0f5ad772872d7aa3b69c90f8f7a4892f6767dd447751450f3598d63d326b35f2")
    version("1.0.2", sha256="fb92ec3235abc21234db89e20c02da0d7b6ac5b3a58a3bbe2175ba4ac20397ee")
    version("1.0.0", sha256="10af147b20eff97b7b0faf3e5ffffc64496b529ebf42a0b5485ff88144eaba0c")
    version("0.9.7", sha256="28bbf9a011abfbba89e8fd78e947cd32644b4c968414051f1fb973d74005e877")
    version("0.9.5.1", sha256="b68dd980819246ee88edb88fc1b9b0ffb7037551c3dd2103361c6d639f6a6e0c")
    version("0.9.3", sha256="2c1cb098ae12b39d0e98b46a2569a94abb5f7324aea093f5be73945a1fca98c7")
    version("0.9.0", sha256="f0d6214a9fa4e430b8bf874dc862a56b74966b17ae354bd761099aeab8edb084")
    version("0.8.9", sha256="4099870c0468aa236ec5b53266a1d02bd2a34685e4e900e400042ba973c607fe")
    version("0.8.5", sha256="741fe805385edb70c40a35acb5d000f98411ece89c1e7ee31b22aedfaf9e1289")
    version("0.8.2", sha256="979bb78e184d2cf4c2cd59918c03b5deb67bbea566b6ba355f12db9f6dc0b59d")
    version("0.8.1", sha256="abb7ba152e7de058b8629152b037701d859b54a069216dd94904c2a9c9c002dd")
    version("0.7.7", sha256="45018942125a80ab6bfde552e0d69b6e29f10bca940caf905249d3f160077016")
    version("0.7.5", sha256="75224173996d4d22e674476f5889006c0fb1fafbdd627d3fb2cc9067ee635b38")
    version("0.7", sha256="f5250bdba8b6a1187b1afd1a178e0ebb8486262ea4be1faf57a748472b6f258e")
    version("0.6", sha256="cc87679af35e55dc9b7b85dcf5143632d28447996a209821ba744a84ea19fbd5")

    depends_on("r-numderiv", type=('build', 'run'))
    depends_on("r-lattice", type=('build', 'run'))
    depends_on("r-mass", type=('build', 'run'))
    depends_on("r-bdsmatrix", type=('build', 'run'))
    depends_on("r-matrix", type=('build', 'run'))
    depends_on("r-mvtnorm", type=('build', 'run'))
