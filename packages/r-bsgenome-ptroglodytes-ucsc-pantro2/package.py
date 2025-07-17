# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePtroglodytesUcscPantro2(RPackage):
    """Full genome sequences for Pan troglodytes (UCSC version panTro2)

    Full genome sequences for Pan troglodytes (Chimp) as provided by UCSC (panTro2, Mar. 2006) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Ptroglodytes.UCSC.panTro2"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro2_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ptroglodytes.UCSC.panTro2/BSgenome.Ptroglodytes.UCSC.panTro2_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="185c9068978611f79a69ff5d1fbaf9eb6560302252d8f4288378e446a954db93",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro2_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
