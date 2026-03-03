# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoftbart(RPackage):
	"""Implements the SoftBart Algorithm

	Implements the SoftBart model of described by Linero and Yang (2018) <doi:10.1111/rssb.12293>, with the optional use of a sparsity-inducing prior to allow for variable selection. For usability, the package maintains the same style as the 'BayesTree' package.
	"""
	
	cran = "SoftBart" 

	version("1.0.1", md5="b57f059244d25713a53bb1407fba6c36")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet@4:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
