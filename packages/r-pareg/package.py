# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPareg(RPackage):
	"""Pathway enrichment using a regularized regression approach

	Compute pathway enrichment scores while accounting for term-term relations. This package uses a regularized multiple linear regression to regress differential expression p-values obtained from multi-condition experiments on a pathway membership matrix. By doing so, it is able to incorporate additional biological knowledge into the enrichment analysis and to estimate pathway enrichment scores more robustly.
	"""
	
	homepage = "https://github.com/cbg-ethz/pareg"
	bioc = "pareg" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pareg_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pareg/pareg_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="f60a1ae8a132d32763c39ae05bbb2364b16ed8446826cf62106d6080ba447233")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tensorflow@2.2:", type=("build", "run"))
	depends_on("r-tfprobability@0.10:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
