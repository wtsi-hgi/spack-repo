# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhastcons100wayUcscHg19(RPackage):
    """UCSC phastCons conservation scores for hg19

    Store UCSC phastCons conservation scores for the human genome (hg19) calculated from multiple alignments with other 99 vertebrate species.
    """

    bioc = "phastCons100way.UCSC.hg19"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons100way.UCSC.hg19_3.7.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/phastCons100way.UCSC.hg19/phastCons100way.UCSC.hg19_3.7.2.tar.gz",
    ]

    version(
        "3.7.2",
        sha256="ca052a0f6e874bcc8079b29e3cc1a29cb6b852b32d5a7a45dea5cff7c924acca",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons100way.UCSC.hg19_3.7.2.tar.gz",
    )

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-genomicscores@1.3.19:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
