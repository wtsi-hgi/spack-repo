# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLboxcox(RPackage):
	"""Implementation of Logistic Box-Cox Regression

	Implements a logistic box-cox model. This model is fully described in Xing, L. et al. (2021) <doi:10.1002/cjs.11587>.
	"""
	
	cran = "lboxcox" 

	version("1.2", md5="3df1ad171a119e51c5f51fa77bf6a9f6")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
