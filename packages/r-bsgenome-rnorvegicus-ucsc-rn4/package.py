# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeRnorvegicusUcscRn4(RPackage):
    """Full genome sequences for Rattus norvegicus (UCSC version rn4)

    Full genome sequences for Rattus norvegicus (Rat) as provided by UCSC (rn4, Nov. 2004) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Rnorvegicus.UCSC.rn4"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn4_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Rnorvegicus.UCSC.rn4/BSgenome.Rnorvegicus.UCSC.rn4_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="ddb876e65948f33f729a81fcb07dda02e5540c58f9ed61690c682decfb129cab",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn4_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
