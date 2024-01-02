# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Verifybamid(CMakePackage):
    """Detecting and estimating inter-sample DNA contamination became a crucial quality assessment step to ensure high quality sequence reads and reliable downstream analysis. Across many existing models, allele frequency usually is used to calculate prior genotype probability. Lack of accurate assignment of allele frequency could result in underestimation of contamination level. Hence we propose this ancestry-agnostic DNA contamination estimation method."""

    homepage = "https://github.com/Griffan/VerifyBamID"
    url = "https://github.com/Griffan/VerifyBamID/archive/refs/tags/2.0.1.tar.gz"

    version("2.0.1", sha256="03c85fa8712324a14b67e59e2c8e42544951f869235b22253fea803b11ca22a4")
    version("1.0.6", sha256="89fad013d8e47f27e6a33a2a977074f9aa9022650d79d0aa3d75694533e9c1d2")
    version("1.0.5", sha256="2083aab615b2e459080fcd88ccc1a9bf50fabb8a4247d37688290ec54e5ce15a")
    version("1.0.4", sha256="69185c49d730a67307efe1714cad403f46709af1b4d835e6b0c084a07b2a20ec")
    version("1.0.3", sha256="0bdc73997ef4a91b2fa6491eb124936cd7677c316478a48cee6bb674a6fe9dc0")
    version("1.0.2", sha256="3768b158e10b18be6334e9995efa39099828f14f9e3f5582e1f100b88de0e832")
    version("1.0.1", sha256="18c91bb9b1696f97a5964611bba48ed395c31977e11384f21d1ded950fadf35e")

    depends_on("htslib")
    depends_on("bzip2")
    depends_on("lzma")
    depends_on("gcc")
    depends_on("pkg-config")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("bin/VerifyBamID", prefix.bin)
