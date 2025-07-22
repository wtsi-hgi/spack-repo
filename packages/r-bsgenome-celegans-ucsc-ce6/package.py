# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCelegansUcscCe6(RPackage):
    """Full genome sequences for Caenorhabditis elegans (UCSC version ce6)

    Full genome sequences for Caenorhabditis elegans (Worm) as provided by UCSC (ce6, May 2008) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Celegans.UCSC.ce6"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce6_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Celegans.UCSC.ce6/BSgenome.Celegans.UCSC.ce6_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="6997709c5f9eca77a1b7d3367bee676f765b672b61acb9471d4cec3eca581f57",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce6_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
