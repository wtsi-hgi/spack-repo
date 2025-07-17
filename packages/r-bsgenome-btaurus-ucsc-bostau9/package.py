# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeBtaurusUcscBostau9(RPackage):
    """Full genome sequences for Bos taurus (UCSC version bosTau9)

    Full genome sequences for Bos taurus (Cow) as provided by UCSC (bosTau9, Apr. 2018) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Btaurus.UCSC.bosTau9"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau9_1.4.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Btaurus.UCSC.bosTau9/BSgenome.Btaurus.UCSC.bosTau9_1.4.2.tar.gz",
    ]

    version(
        "1.4.2",
        sha256="efc45fc133c6c502ed3c769d5eb70689c8514f35604c871bc6cb2b1740f8a96f",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau9_1.4.2.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
