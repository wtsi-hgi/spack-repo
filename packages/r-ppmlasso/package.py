# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpmlasso(RPackage):
	"""Point Process Models with LASSO-Type Penalties

	Toolkit for fitting point process models with sequences of LASSO penalties ("regularisation paths"), as described in Renner, I.W. and Warton, D.I. (2013) <doi:10.1111/j.1541-0420.2012.01824.x>. Regularisation paths of Poisson point process models or area-interaction models can be fitted with LASSO, adaptive LASSO or elastic net penalties. A number of criteria are available to judge the bias-variance tradeoff.
	"""
	
	cran = "ppmlasso" 

	version("1.4", md5="a9137e20003581a84d5833d7ea867a95")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spatstat@3.0.0:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
