# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePtroglodytesUcscPantro6(RPackage):
    """Full genome sequences for Pan troglodytes (UCSC version panTro6)

    Full genome sequences for Pan troglodytes (Chimp) as provided by UCSC (panTro6, Jan. 2018) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Ptroglodytes.UCSC.panTro6"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro6_1.4.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ptroglodytes.UCSC.panTro6/BSgenome.Ptroglodytes.UCSC.panTro6_1.4.2.tar.gz",
    ]

    version(
        "1.4.2",
        sha256="0be0565fa5937fe2d4da5e247f8deecce0dd76a8606dbfe75162e118b8c52ed0",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro6_1.4.2.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
