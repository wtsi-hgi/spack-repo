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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BayesSpace_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BayesSpace/BayesSpace_1.12.0.tar.gz"]

	version("1.12.0", sha256="0584268335dad3b79815c1a85201167585b1258cff171bd949c1ed6ca9d70fd7")

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
