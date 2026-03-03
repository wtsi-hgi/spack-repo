# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsebiplots(RPackage):
	"""'HJ-Biplot' using Different Ways of Penalization Plotting with
'ggplot2'

	'HJ-Biplot' is a multivariate method that allow represent multivariate data on a subspace of low dimension, in such a way that most of the variability of the information is captured in a few dimensions. This package implements three new techniques and constructs in each case the 'HJ-Biplot', adapting restrictions to reduce weights and / or produce zero weights in the dimensions, based on the regularization theories. It implements three methods of regularization: Ridge, LASSO and Elastic Net.
	"""
	
	homepage = "https://github.com/mitzicubillamontilla/SparseBiplots"
	cran = "SparseBiplots" 

	version("4.0.1", md5="a5c37eab5f0215b4a0c7d613e4e901e6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sparsepca", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
