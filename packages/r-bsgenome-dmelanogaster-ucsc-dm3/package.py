# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDmelanogasterUcscDm3(RPackage):
    """Full genome sequences for Drosophila melanogaster (UCSC version dm3)

    Full genome sequences for Drosophila melanogaster (Fly) as provided by UCSC (dm3, Apr. 2006) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Dmelanogaster.UCSC.dm3"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm3_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Dmelanogaster.UCSC.dm3/BSgenome.Dmelanogaster.UCSC.dm3_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="68ebdefa8c99330f320d1928673ac89601e842102990cbed1b4f4d08271d75a5",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm3_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
