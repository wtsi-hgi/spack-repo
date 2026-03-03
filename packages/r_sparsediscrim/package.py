# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsediscrim(RPackage):
	"""Sparse and Regularized Discriminant Analysis

	A collection of sparse and regularized discriminant analysis
    methods intended for small-sample, high-dimensional data sets. The package
    features the High-Dimensional Regularized Discriminant Analysis classifier
    from Ramey et al. (2017) <arXiv:1602.01182>. Other classifiers include
    those from Dudoit et al. (2002) <doi:10.1198/016214502753479248>, Pang et
    al. (2009) <doi:10.1111/j.1541-0420.2009.01200.x>, and Tong et al. (2012)
    <doi:10.1093/bioinformatics/btr690>.
	"""
	
	homepage = "https://github.com/topepo/sparsediscrim"
	cran = "sparsediscrim" 

	version("0.3.0", md5="4cdd10c59df28829154258345ceb5e0e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
