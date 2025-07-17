# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApalyzer(RPackage):
    """A toolkit for APA analysis using RNA-seq data

    Perform 3'UTR APA, Intronic APA and gene expression analysis using RNA-seq data.
    """

    homepage = "https://github.com/RJWANGbioinfo/APAlyzer/"
    bioc = "APAlyzer"

    version("1.22.0", commit="a1ea9dfbabf37b7f70671f6e651234415732a672")
    version("1.16.0", commit="9a02db164423269fe717204b9dc9ce62b5141d12")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rsubread", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-repmis", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-hybridmtest", type=("build", "run"))
