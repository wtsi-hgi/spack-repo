# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScclassify(RPackage):
	"""scClassify: single-cell Hierarchical Classification

	scClassify is a multiscale classification framework for single-cell RNA-seq data based on ensemble learning and cell type hierarchies, enabling sample size estimation required for accurate cell type classification and joint classification of cells using multiple references.
	"""
	
	bioc = "scClassify" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scClassify_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scClassify/scClassify_1.14.0.tar.gz"]

	version("1.14.0", sha256="6ed52ca8d4839c48a9812b752350865ba0c793382b44289e04a26037b22b84c6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hopach", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-cepo", type=("build", "run"))
