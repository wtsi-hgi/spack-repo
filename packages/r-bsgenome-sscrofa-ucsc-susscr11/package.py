# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeSscrofaUcscSusscr11(RPackage):
    """Full genome sequences for Sus scrofa (UCSC version susScr11)

    Full genome sequences for Sus scrofa (Pig) as provided by UCSC (susScr11, Feb. 2017) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Sscrofa.UCSC.susScr11"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Sscrofa.UCSC.susScr11_1.4.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Sscrofa.UCSC.susScr11/BSgenome.Sscrofa.UCSC.susScr11_1.4.2.tar.gz",
    ]

    version(
        "1.4.2",
        sha256="9821dbdeaec06cd4f83a20b370d97062ca8eda43e1fbdea795795c4c4e16ec54",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Sscrofa.UCSC.susScr11_1.4.2.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
