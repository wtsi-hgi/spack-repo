# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGencodegenes(PythonPackage):
    """Package to load genes from GENCODE GTF files"""

    homepage = "https://github.com/jeremymcrae/gencodegenes"
    pypi = "gencodegenes/gencodegenes-1.1.4.tar.gz"

    version("0.9.15", sha256="babb87cd6978d3a78f91ccb7283e7664cbd029956b3990f91ae3af99abfaccf7")
    version("1.0.0", sha256="e2850e471ba47395c8ee931288cb924a86f3610f28d39e2b0d48c9de770261ac")
    version("1.0.1", sha256="aeff07c95e2f44b80f3809fd1371c72c13eea5b186d62091e001214e6e471319")
    version("1.0.10", sha256="ad50af52fbf92a2efb9c4678a9d0e6cc1e411b97f4b5c85028c85eb3cad89854")
    version("1.0.2", sha256="26f6f0762def197820532cff3e320a1a8617e591616443746a6fb59a6f7fa7c6")
    version("1.0.4", sha256="e77c7f016c75da681ec5baf334041e9d28bc088c019ef533c8fc8f708865dc71")
    version("1.0.5", sha256="8046a0d4d9621358183a6eadc94b4a07a7f039fb0a1453b177e4b0d9bf32fb61")
    version("1.0.6", sha256="f92fd897eeeef1030fc88d32f7571dca94973a4a18bcb69bc6d2f058dd1ab89f")
    version("1.0.7", sha256="b8dcff27bc478d7e791dc0c23fba5d30708369cdd7970d2a1e7139ce9aae6300")
    version("1.0.8", sha256="744af12565292171ac7bac41f009d11829853918e8d776da0ff3bf50a7f637da")
    version("1.0.9", sha256="4faba62c1cf700e0accb9ab08434e9dd780d2fc4109171821dfb3f087e4b465e")
    version("1.1.0", sha256="eb1603f819d85cd4b70a440328e940f865a7e646078e477c86aa34bfaf23747d")
    version("1.1.1", sha256="8f8f2a117f06707c2b4dd41d5082386f9c678829718b15989eff0432a1338fd9")
    version("1.1.2", sha256="e5c827dfc45a4d41e0537706f75a501f12e3882a78c9b2468a75bb4c7a537310")
    version("1.1.4", sha256="a5096260bedff7fd703642c11e77ba0f37edbfa71e3b4f57ba6d5b98175ba582")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("py-cython", type="build")
    depends_on("zlib")
