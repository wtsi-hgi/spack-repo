# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePtroglodytesUcscPantro3(RPackage):
    """Full genome sequences for Pan troglodytes (UCSC version panTro3)

    Full genome sequences for Pan troglodytes (Chimp) as provided by UCSC (panTro3, Oct. 2010) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Ptroglodytes.UCSC.panTro3"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro3_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ptroglodytes.UCSC.panTro3/BSgenome.Ptroglodytes.UCSC.panTro3_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="f51d7702c8255bb470b774088124f3b956b063eb09e05035e32c13993fe86eed",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro3_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
