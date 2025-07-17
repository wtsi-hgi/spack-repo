# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeScerevisiaeUcscSaccer2(RPackage):
    """Saccharomyces cerevisiae (Yeast) full genome (UCSC version sacCer2)

    Saccharomyces cerevisiae (Yeast) full genome as provided by UCSC (sacCer2, June 2008) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Scerevisiae.UCSC.sacCer2"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Scerevisiae.UCSC.sacCer2_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Scerevisiae.UCSC.sacCer2/BSgenome.Scerevisiae.UCSC.sacCer2_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="6092af9e3e10248447fa41303e53c56798685e791080afeb5533868e8d189fc6",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Scerevisiae.UCSC.sacCer2_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
