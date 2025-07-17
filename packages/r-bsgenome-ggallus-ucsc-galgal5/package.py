# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeGgallusUcscGalgal5(RPackage):
    """Full genome sequences for Gallus gallus (UCSC version galGal5)

    Full genome sequences for Gallus gallus (Chicken) as provided by UCSC (galGal5, Dec. 2015) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Ggallus.UCSC.galGal5"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal5_1.4.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ggallus.UCSC.galGal5/BSgenome.Ggallus.UCSC.galGal5_1.4.2.tar.gz",
    ]

    version(
        "1.4.2",
        sha256="abc9f105c4386840d325c273816a1ea6cbc7c6c5d52260221fd68d257217283e",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal5_1.4.2.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
