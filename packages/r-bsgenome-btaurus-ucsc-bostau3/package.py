# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeBtaurusUcscBostau3(RPackage):
    """Full genome sequences for Bos taurus (UCSC version bosTau3)

    Full genome sequences for Bos taurus (Cow) as provided by UCSC (bosTau3, Aug. 2006) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Btaurus.UCSC.bosTau3"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau3_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Btaurus.UCSC.bosTau3/BSgenome.Btaurus.UCSC.bosTau3_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="ecfe01dcbe0707b98a3f72536d4baccc02480e148fdf610e77d6df838931036e",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau3_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
