# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiftHsapiensDbsnp137(RPackage):
    """PROVEAN/SIFT Predictions for Homo sapiens dbSNP build 137

    Database of PROVEAN/SIFT predictions for Homo sapiens dbSNP build 137
    """

    bioc = "SIFT.Hsapiens.dbSNP137"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SIFT.Hsapiens.dbSNP137_1.0.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SIFT.Hsapiens.dbSNP137/SIFT.Hsapiens.dbSNP137_1.0.0.tar.gz",
    ]

    version(
        "1.0.0",
        sha256="48d25a7afcd0107dde7bb57a946ce068b2f3e0efa1a06cbd8f9f2fabf052e290",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SIFT.Hsapiens.dbSNP137_1.0.0.tar.gz",
    )

    depends_on("r-variantannotation@1.9.15:", type=("build", "run"))
    depends_on("r-rsqlite@0.11:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
