# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman370v1ccrlmm(RPackage):
    """Metadata for fast genotyping with the 'crlmm' package

    Package with metadata for genotyping Illumina 370k arrays using the 'crlmm' package.
    """

    bioc = "human370v1cCrlmm"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human370v1cCrlmm_1.0.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human370v1cCrlmm/human370v1cCrlmm_1.0.2.tar.gz",
    ]

    version(
        "1.0.2",
        sha256="c735a7d7b383d61d359cd94b0418e5ab242aa7f6922f443376c843780d7b1bba",
    )
