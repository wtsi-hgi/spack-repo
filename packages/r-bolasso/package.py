# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBolasso(RPackage):
	"""Model Consistent Lasso Estimation Through the Bootstrap

	Implements the bolasso algorithm for consistent variable selection 
    and estimation accuracy. Includes support for many parallel backends via the 
    future package. For details see: Bach (2008),
    'Bolasso: model consistent Lasso estimation through the bootstrap', 
    <arXiv:0804.1302>.
	"""
	
	homepage = "https://www.dmolitor.com/bolasso/"
	cran = "bolasso" 

	version("0.2.0", md5="cc75e36ee639b5d39781a83765fe22ec")

	depends_on("r-matrix@1.0.6:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-future-apply@1.1:", type=("build", "run"))
	depends_on("r-gamlr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet@3:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
