# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiospear(RPackage):
	"""Biomarker Selection in Penalized Regression Models

	Provides some tools for developing and validating prediction models, estimate expected survival of patients and visualize them graphically. Most of the implemented methods are based on penalized regressions such as: the lasso (Tibshirani R (1996)), the elastic net (Zou H et al. (2005) <doi:10.1111/j.1467-9868.2005.00503.x>), the adaptive lasso (Zou H (2006) <doi:10.1198/016214506000000735>), the stability selection (Meinshausen N et al. (2010) <doi:10.1111/j.1467-9868.2010.00740.x>), some extensions of the lasso (Ternes et al. (2016) <doi:10.1002/sim.6927>), some methods for the interaction setting (Ternes N et al. (2016) <doi:10.1002/bimj.201500234>), or others. A function generating simulated survival data set is also provided.
	"""
	
	cran = "biospear" 

	version("1.0.2", md5="196e76b33e56a272dc4fa0d720d1b799")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pkgconfig", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-grplasso", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-plsrcox", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-survauc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
