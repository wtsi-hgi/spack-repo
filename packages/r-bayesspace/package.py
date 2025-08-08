# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesspace(RPackage):
    """Clustering and Resolution Enhancement of Spatial Transcriptomes

    Tools for clustering and enhancing the resolution of spatial gene expression experiments. BayesSpace clusters a low-dimensional representation of the gene expression matrix, incorporating a spatial prior to encourage neighboring spots to cluster together. The method can enhance the resolution of the low-dimensional representation into "sub-spots", for which features such as gene expression or cell type composition can be imputed.
    """

    homepage = "edward130603.github.io/BayesSpace"
    bioc = "BayesSpace"

    version("1.18.3", commit="28484b2a2257043e2ca08a310e3f6ad7576e7cc1")
    version("1.12.0", commit="1e3042dfc99bc5b66f55872164ed5c2de5572b9d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-dirichletreg", type=("build", "run"))
    depends_on("r-xgboost", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-rcppdist", type=("build", "run"))
    depends_on("r-rcppprogress", type=("build", "run"))
    depends_on("r-arrow", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-microbenchmark", type=("build", "run"))
