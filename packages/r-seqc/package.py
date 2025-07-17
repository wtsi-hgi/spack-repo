# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqc(RPackage):
    """RNA-seq data generated from SEQC (MAQC-III) study

    The SEQC/MAQC-III Consortium has produced benchmark RNA-seq data for the assessment of RNA sequencing technologies and data analysis methods (Nat Biotechnol, 2014). Billions of sequence reads have been generated from ten different sequencing sites. This package contains the summarized read count data for ~2000 sequencing libraries. It also includes all the exon-exon junctions discovered from the study. TaqMan RT-PCR data for ~1000 genes and ERCC spike-in sequence data are included in this package as well.
    """

    bioc = "seqc"

    version("1.42.0", commit="9507cc9f535e70aa3833ff34e5507d426d3dc1e6")
    version("1.36.0", commit="8a938877867a1a74b0915fa09777a32f904b29e3")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
