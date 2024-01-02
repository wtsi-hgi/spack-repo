# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSplus2r(RPackage):
    """Currently there are many functions in S-PLUS that are missing in R. To facilitate the conversion of S-PLUS packages to R packages, this package provides some missing S-PLUS functionality in R."""

    homepage = "https://github.com/spkaluzny/splus2r"
    cran = "splus2R"

    version("1.3-3", sha256="7d5c90842debaf6046d445e3fce4f9721baad0339aa7193339705ef68568bf0c")
    version("1.2-2", sha256="5f1b3c3fc3bea998ef91478742d9215cc2d1c2d94ba17a2834ec02df37922b77")
    version("1.2-1", sha256="7e17145378fcffa4936ab5b015c300bb340da0470f4ac24e2a4fb5f4880d170f")
    version("1.2-0", sha256="615f447bb16b03eb9ee0c7f633a4afa5870dcf7f7bf33f51281540ff55c8be4e")
    version("1.1-3", sha256="2566a9b02faa5528ec127ab372d9b4550839f64be3a0eb2b998637b99264b29d")
    version("1.1-2", sha256="276f315b60a297257a3425138a9d5553b1b5a1bc8434407ffe3be39452f2caf5")
    version("1.1-1", sha256="44bc7ddb41833d60490d41ad92333e2c637460dfa77e2a32f19a2a8536263125")
    version("1.1-0", sha256="d2dee3cfe8f400eb220fa06718fb8f6bcaf79f9fc6f2f332c4537ec298128c82")
    version("1.0-6", sha256="860f4ef15063238595eaf4a851540df1c5d2be73ca7aa19d5bd354b9fac51d76")
    version("1.0-5", sha256="1ce467acfadbc051ac0e40eae6ade867ac52573332a30d55c89c1c60733d7f8d")
    version("1.0-3", sha256="09fba3045d173dbc715216c0d7ecc739721ac21a2f28eba13476120f13034bd7")
    version("1.0-2", sha256="2d48e8b5acd86877b96379fdc1861f12d018fff6acdd88e6329528f58f127981")
    version("1.0-1", sha256="9c33babc1a444d65b828da2342da4c640016995fd1afbb1954f80524da53e0a7")
    version("1.0", sha256="fd7c86435688666c0aa1d66735d48d33ea4c67517af75db9e208d12060dbdc5f")
