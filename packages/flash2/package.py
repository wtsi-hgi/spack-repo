# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Flash2(MakefilePackage):
    """FLASH2 (Fast Length Adjustment of SHort reads) is an improved version of FLASH
    for merging paired-end reads that were generated from DNA fragments. It includes
    new logic for innie and outie overlaps as well as initial steps for handling
    amplicons."""

    homepage = "https://github.com/dstreett/FLASH2"
    url = "https://github.com/dstreett/FLASH2/archive/refs/tags/2.2.00.tar.gz"

    version("2.2.00", sha256="7bb357a935de87be8a294b35ed281eca2e08afa1e1a1d1b1c24a024b80b713ff")

    depends_on("zlib")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("flash2", prefix.bin)

    def build(self, spec, prefix):
        make()
