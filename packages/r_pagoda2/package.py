# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagoda2(RPackage):
	"""Single Cell Analysis and Differential Expression

	Analyzing and interactively exploring large-scale single-cell RNA-seq datasets. 'pagoda2' primarily performs normalization and differential gene expression analysis, with an interactive application for exploring single-cell RNA-seq datasets. It performs basic tasks such as cell size normalization, gene variance normalization, and can be used to identify subpopulations and run differential expression within individual samples. 'pagoda2' was written to rapidly process modern large-scale scRNAseq datasets of approximately 1e6 cells. The companion web application allows users to explore which gene expression patterns form the different subpopulations within your data. The package also serves as the primary method for preprocessing data for conos, <https://github.com/kharchenkolab/conos>. This package interacts with data available through the 'p2data' package, which is available in a 'drat' repository. To access this data package, see the instructions at <https://github.com/kharchenkolab/pagoda2>. The size of the 'p2data' package is approximately 6 MB.
	"""
	
	homepage = "https://github.com/kharchenkolab/pagoda2"
	cran = "pagoda2" 

	version("1.0.12", md5="9ecefd8a29f040f5df0b56351948522a", url="https://cran.r-project.org/src/contrib/pagoda2_1.0.12.tar.gz")
	version("1.0.11", md5="c2abb2ed7da8c7a1c91bd9158df678cc", url="https://cran.r-project.org/src/contrib/pagoda2_1.0.11.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dendsort", type=("build", "run"))
	depends_on("r-drat", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-n2r", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rmtstat", type=("build", "run"))
	depends_on("r-rook", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-sccore@0.1.1:", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
