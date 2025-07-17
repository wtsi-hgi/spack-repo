# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgacrcmrna(RPackage):
    """TCGA CRC 450 mRNA dataset

    colorectal cancer mRNA profile provided by TCGA
    """

    bioc = "TCGAcrcmRNA"

    version("1.28.0", commit="32c742f95a0a8841b159d2a6ac62b9d60053a0b3")
    version("1.22.0", commit="ccf8957b01d11c73d3bbf1df41db1b4b73d0427d")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
