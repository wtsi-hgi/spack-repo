# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBestglm(RPackage):
	"""Best Subset GLM and Regression Utilities

	Best subset glm using information criteria or cross-validation,
        carried by using 'leaps' algorithm (Furnival and Wilson, 1974) <doi:10.2307/1267601>
        or complete enumeration (Morgan and Tatar, 1972) <doi:10.1080/00401706.1972.10488918>.
        Implements PCR and PLS using AIC/BIC.
        Implements one-standard deviation rule for use with the 'caret' package.
	"""
	
	cran = "bestglm" 

	version("0.37.3", md5="914b9c33e4b2a76b778d53935565ba4f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
