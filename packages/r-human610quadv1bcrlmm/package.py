# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman610quadv1bcrlmm(RPackage):
    """Metadata for fast genotyping with the 'crlmm' package

    Package with metadata for genotyping Illumina 610kQuad arrays using the 'crlmm' package.
    """

    bioc = "human610quadv1bCrlmm"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human610quadv1bCrlmm_1.0.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human610quadv1bCrlmm/human610quadv1bCrlmm_1.0.3.tar.gz",
    ]

    version(
        "1.0.3",
        sha256="04dbfb5a4eb5aaf84f524aac48359ba3f16f55db695d9d26ca8678c8ffdd1775",
    )
