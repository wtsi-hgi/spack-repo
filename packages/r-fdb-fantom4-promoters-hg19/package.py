# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdbFantom4PromotersHg19(RPackage):
    """Annotation package for FANTOM4 promoters identified from THP-1 cells

    FANTOM4 promoters, liftOver'ed from hg18 to hg19, CpGs quantified
    """

    bioc = "FDb.FANTOM4.promoters.hg19"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.FANTOM4.promoters.hg19_1.0.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/FDb.FANTOM4.promoters.hg19/FDb.FANTOM4.promoters.hg19_1.0.0.tar.gz",
    ]

    version(
        "1.0.0",
        sha256="3ca3cfe22ec6cc576ef8587383e6cad07ff481df2b58c33f7c8bb992432f5613",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.FANTOM4.promoters.hg19_1.0.0.tar.gz",
    )

    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
