# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhm(RPackage):
	"""Additive Heredity Model: Method for the Mixture-of-Mixtures
Experiments

	An implementation of the additive heredity model for the mixture-of-mixtures experiments of Shen et al. (2019) in Technometrics <doi:10.1080/00401706.2019.1630010>. The additive heredity model considers an additive structure to inherently connect the major components with the minor components. The additive heredity model has a meaningful interpretation for the estimated model because of the hierarchical and heredity principles applied and the nonnegative garrote technique used for variable selection. 
	"""
	
	cran = "AHM" 

	version("1.0.1", md5="c44632e33ad5e9373cb88a0f14c8b268")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mixexp", type=("build", "run"))
	depends_on("r-plgp", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
