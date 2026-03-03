# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbknnr(RPackage):
	"""Perform Batch Balanced KNN in R

	A fast and intuitive batch effect removal tool for single-cell data. BBKNN is originally used in the 'scanpy' python package, and now can be used with 'Seurat' seamlessly.
	"""
	
	homepage = "https://github.com/ycli1995/bbknnR"
	cran = "bbknnR" 

	version("1.1.1", md5="bb7a78d917fac087af38150afb33b7fe")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp@1.0.8:", type=("build", "run"))
	depends_on("r-rcppannoy", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
	depends_on("r-tidytable", type=("build", "run"))
	depends_on("r-uwot@0.1.14:", type=("build", "run"))
