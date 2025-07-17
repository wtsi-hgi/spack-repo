# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman550v3bcrlmm(RPackage):
    """Metadata for fast genotyping with the 'crlmm' package

    Package with metadata for genotyping Illumina 550k arrays using the 'crlmm' package.
    """

    bioc = "human550v3bCrlmm"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human550v3bCrlmm_1.0.4.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human550v3bCrlmm/human550v3bCrlmm_1.0.4.tar.gz",
    ]

    version(
        "1.0.4",
        sha256="18cce90e1e43e98cedc5c7e5601fa0a51579e91ec1116cbc1cbdd026216b4705",
    )
