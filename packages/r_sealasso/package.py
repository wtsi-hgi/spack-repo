# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSealasso(RPackage):
	"""Standard Error Adjusted Adaptive Lasso

	Standard error adjusted adaptive lasso (SEA-lasso) is a version of the adaptive lasso, which incorporates OLS standard error to the L1 penalty weight. This method is intended for variable selection under linear regression settings (n > p). This new weight assignment strategy is especially useful when the collinearity of the design matrix is a concern. 
	"""
	
	cran = "sealasso" 

	version("0.1-3", md5="0bfa41b7e1417fe5c3ffa088424a41a4")

	depends_on("r@2.9.1:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
