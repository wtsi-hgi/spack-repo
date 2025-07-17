# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDrerioUcscDanrer5(RPackage):
    """Full genome sequences for Danio rerio (UCSC version danRer5)

    Full genome sequences for Danio rerio (Zebrafish) as provided by UCSC (danRer5, Jul. 2007) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Drerio.UCSC.danRer5"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer5_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Drerio.UCSC.danRer5/BSgenome.Drerio.UCSC.danRer5_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="65031c68852bcebc47c169bc84a85e9bed7996ddde7a9de9ee22053523f1b5d7",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer5_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
