# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMispr(RPackage):
	"""Multiple Imputation with Sequential Penalized Regression

	Generates multivariate imputations using sequential regression with L2 penalty. For more details see Zahid and Heumann (2018) <doi:10.1177/0962280218755574>.
	"""
	
	cran = "mispr" 

	version("1.0.0", md5="959c64bb7550792a5f663d09b6291b6a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
