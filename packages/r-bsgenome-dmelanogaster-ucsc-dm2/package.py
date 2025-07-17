# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDmelanogasterUcscDm2(RPackage):
    """Full genome sequences for Drosophila melanogaster (UCSC version dm2)

    Full genome sequences for Drosophila melanogaster (Fly) as provided by UCSC (dm2, Apr. 2004) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Dmelanogaster.UCSC.dm2"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm2_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Dmelanogaster.UCSC.dm2/BSgenome.Dmelanogaster.UCSC.dm2_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="d4f21a961fa4f038dfe7f17cefe2361268496ec8cf7b1e83bdf50f11425dd8ee",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dmelanogaster.UCSC.dm2_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
