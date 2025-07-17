# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdbUcscSnp135commonHg19(RPackage):
    """UCSC common SNPs track for dbSNP build 135

    makeFeatureDbFromUCSC cannot cope with this track, hence a package
    """

    bioc = "FDb.UCSC.snp135common.hg19"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.UCSC.snp135common.hg19_1.0.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/FDb.UCSC.snp135common.hg19/FDb.UCSC.snp135common.hg19_1.0.0.tar.gz",
    ]

    version(
        "1.0.0",
        sha256="b7cf877170f5bd3bcfe1eafa49e8dfaca88a0cc85c065e4c97ca20be728f7efa",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.UCSC.snp135common.hg19_1.0.0.tar.gz",
    )

    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
