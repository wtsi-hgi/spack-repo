# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegnorm(RPackage):
    """DegNorm: degradation normalization for RNA-seq data

    This package performs degradation normalization in bulk RNA-seq data to improve differential expression analysis accuracy.
    """

    bioc = "DegNorm"

    version("1.18.0", commit="0d4cbd394552c87e76519e4a834f18d43a5ed9c5")
    version("1.12.0", commit="405e5cbde57005915a61b65daa5c2e85f794e67d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-heatmaply", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
