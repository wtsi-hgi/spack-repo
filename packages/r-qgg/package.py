# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgg(RPackage):
	"""Statistical Tools for Quantitative Genetic Analyses

	Provides an infrastructure for efficient processing of large-scale genetic and phenotypic data including core functions for: 1) fitting linear mixed models, 2) constructing marker-based genomic relationship matrices, 3) estimating genetic parameters (heritability and correlation), 4) performing genomic prediction and genetic risk profiling, and 5) single or multi-marker association analyses.
    Rohde et al. (2019) <doi:10.1101/503631>.
	"""
	
	homepage = "https://github.com/psoerensen/qgg"
	cran = "qgg" 

	version("1.1.2", md5="2f47dcdff220e6fcec7cd0106e14e8a3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
