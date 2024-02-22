# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmerpack(RPackage):
	"""Tools of Heterogeneity Pursuit via Finite Mixture Effects Model

	Heterogeneity pursuit methodologies for regularized finite mixture regression by effects-model formulation proposed by Li et al. (2021) <arXiv:2003.04787>.
	"""
	
	cran = "fmerPack" 

	version("0.0-1", md5="1fc0742ee7739256e4cced0acd93b138")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
