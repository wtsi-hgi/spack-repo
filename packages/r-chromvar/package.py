# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromvar(RPackage):
    """Chromatin Variation Across Regions

    Determine variation in chromatin accessibility across sets of annotations or peaks. Designed primarily for single-cell or sparse chromatin accessibility data, e.g. from scATAC-seq or sparse bulk ATAC or DNAse-seq experiments.
    """

    bioc = "chromVAR"
    version("1.30.1", commit="c6c5a2cd718fb0bf95b928800133a072c275e8b7")
    version("1.24.0", commit="e2d61b06f8582c97ea83f351757aca9770638a2a")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-nabor", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-tfbstools", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-miniui", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
