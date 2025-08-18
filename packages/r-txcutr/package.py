# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxcutr(RPackage):
    """Transcriptome CUTteR

    Various mRNA sequencing library preparation methods generate sequencing reads specifically from the transcript ends. Analyses that focus on quantification of isoform usage from such data can be aided by using truncated versions of transcriptome annotations, both at the alignment or pseudo-alignment stage, as well as in downstream analysis. This package implements some convenience methods for readily generating such truncated annotations and their corresponding sequences.
    """

    bioc = "txcutr"

    version("1.14.0", commit="458693b7720be1deaf7c5a17f4d05fd6c2a2ec47")
    version("1.8.0", commit="9478f70277fe26324d23e934826d4e27b4677446")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    # txcutr imports and uses txdbmaker at runtime
    depends_on("r-txdbmaker", type=("build", "run"))
