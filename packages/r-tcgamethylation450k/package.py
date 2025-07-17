# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgamethylation450k(RPackage):
    """The Cancer Genome Atlas Illumina 450k methylation example data

    The Cancer Genome Atlas (TCGA) is applying genomics technologies to over 20 different types of cancer.  This package contains a small set of 450k array data in idat format.
    """

    bioc = "TCGAMethylation450k"

    version("1.44.0", commit="3c04710584d1689712b81fb6dfbe3c07cd3eff3c")
    version("1.38.0", commit="12d29f26d5fc2093884753cea8e2d4650a2c7595")
