# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimputation(RPackage):
	"""Simple Imputation

	Easy to use interfaces to a number of imputation methods
        that fit in the not-a-pipe operator of the 'magrittr' package.
	"""
	
	homepage = "https://github.com/markvanderloo/simputation"
	cran = "simputation" 

	version("0.2.8", md5="e4931cd1bb8c5db18bfd37daf5c84c3b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-gower", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
