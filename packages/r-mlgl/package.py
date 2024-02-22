# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlgl(RPackage):
	"""Multi-Layer Group-Lasso

	It implements a new procedure of variable selection in the context of redundancy between explanatory variables, which holds true with high dimensional data (Grimonprez et al. (2023) <doi:10.18637/jss.v106.i03>).
	"""
	
	cran = "MLGL" 

	version("1.0.0", md5="fccc1f35a3edd29f1c3bf2df761e00d7")

	depends_on("r-gglasso", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
