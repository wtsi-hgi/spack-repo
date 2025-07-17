# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDrerioUcscDanrer7(RPackage):
    """Full genome sequences for Danio rerio (UCSC version danRer7)

    Full genome sequences for Danio rerio (Zebrafish) as provided by UCSC (danRer7, Jul. 2010) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Drerio.UCSC.danRer7"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer7_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Drerio.UCSC.danRer7/BSgenome.Drerio.UCSC.danRer7_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="ef2e7e27508d7dbfc63e09ae36f96d2578590af1f12b82912fe029898084a39f",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer7_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
