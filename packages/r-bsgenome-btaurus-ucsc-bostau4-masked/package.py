# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeBtaurusUcscBostau4Masked(RPackage):
    """Full masked genome sequences for Bos taurus (UCSC version bosTau4)

    Full genome sequences for Bos taurus (Cow) as provided by UCSC (bosTau4, Oct. 2007) and stored in Biostrings objects. The sequences are the same as in BSgenome.Btaurus.UCSC.bosTau4, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
    """

    bioc = "BSgenome.Btaurus.UCSC.bosTau4.masked"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau4.masked_1.3.99.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Btaurus.UCSC.bosTau4.masked/BSgenome.Btaurus.UCSC.bosTau4.masked_1.3.99.tar.gz",
    ]

    version(
        "1.3.99",
        sha256="f999b71c1c55a63ea7ee5ba8d2aa9ba249bbb2d3438d7176a0a917d57b4c7f36",
    )

    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-bsgenome-btaurus-ucsc-bostau4", type=("build", "run"))
