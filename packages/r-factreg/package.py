# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactreg(RPackage):
	"""Multi-Environment Genomic Prediction with Penalized Factorial
Regression

	Multi-environment genomic prediction for training and test 
    environments using penalized factorial regression. Predictions are made 
    using genotype-specific environmental sensitivities as in Millet et al. 
    (2019) <doi:10.1038/s41588-019-0414-y>.
	"""
	
	cran = "factReg" 

	version("1.0.0", md5="4214ad8966a0f4a7321357576d2de80e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rrblup", type=("build", "run"))
