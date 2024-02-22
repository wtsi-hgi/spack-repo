# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTca(RPackage):
	"""Tensor Composition Analysis

	Tensor Composition Analysis (TCA) allows the deconvolution of two-dimensional data (features by observations) coming from a mixture of heterogeneous sources into a three-dimensional matrix of signals (features by observations by sources). The TCA framework further allows to test the features in the data for different statistical relations with an outcome of interest while modeling source-specific effects; particularly, it allows to look for statistical relations between source-specific signals and an outcome. For example, TCA can deconvolve bulk tissue-level DNA methylation data (methylation sites by individuals) into a three-dimensional tensor of cell-type-specific methylation levels for each individual (i.e. methylation sites by individuals by cell types) and it allows to detect cell-type-specific statistical relations (associations) with phenotypes. For more details see Rahmani et al. (2019) <DOI:10.1038/s41467-019-11052-9>.
	"""
	
	homepage = "https://www.nature.com/articles/s41467-019-11052-9"
	cran = "TCA" 

	version("1.2.1", md5="cfd6fc03ef50d2b7685ee902f44d8ef6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
