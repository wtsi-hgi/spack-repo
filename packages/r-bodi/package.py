# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBodi(RPackage):
	"""Boosting Diversity in Regression Ensembles

	A gradient boosting-based algorithm by incorporating a diversity term to guide the gradient boosting iterations, see Bourel, Cugliari, Goude, Poggi (2021) <https://hal.archives-ouvertes.fr/hal-03041309/>.
	"""
	
	cran = "Bodi" 

	version("0.1.0", md5="d12c58a7d4ba8890d406c065f0c0942c")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-opera", type=("build", "run"))
