# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxrobust(RPackage):
	"""Fit Robustly Proportional Hazards Regression Model

	An implementation of robust estimation in Cox model. Functionality includes fitting efficiently and robustly Cox proportional hazards regression model in its basic form, where explanatory variables are time independent with one event per subject.  Method is based on a smooth modification of the partial likelihood.
	"""
	
	homepage = "https://github.com/ShanaScogin/coxrobust"
	cran = "coxrobust" 

	version("1.0.1", md5="028da5f3ca518b240f4efd013bf0b8c2")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
