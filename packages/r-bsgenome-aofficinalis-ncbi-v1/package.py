# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAofficinalisNcbiV1(RPackage):
    """Asparagus officinalis (Garden asparagus) full genome (NCBI version Aspof.V1)

    Full genome sequences for Asparagus officinalis (Garden asparagus) as provided by NCBI (Aspof.V1, Feb. 2017) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Aofficinalis.NCBI.V1"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Aofficinalis.NCBI.V1_1.0.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Aofficinalis.NCBI.V1/BSgenome.Aofficinalis.NCBI.V1_1.0.0.tar.gz",
    ]

    version(
        "1.0.0",
        sha256="5966d0f851667db14191871c198e404d28d8273669e8b30cd9cbfc78ad2cd558",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Aofficinalis.NCBI.V1_1.0.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
