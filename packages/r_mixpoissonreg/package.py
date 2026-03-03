# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixpoissonreg(RPackage):
	"""Mixed Poisson Regression for Overdispersed Count Data

	Fits mixed Poisson regression models (Poisson-Inverse Gaussian or Negative-Binomial) on data sets with response variables being count data. The models can have varying precision parameter, where a linear regression structure (through a link function) is assumed to hold on the precision parameter. The Expectation-Maximization algorithm for both these models (Poisson Inverse Gaussian and Negative Binomial) is an important contribution of this package. Another important feature of this package is the set of functions to perform global and local influence analysis. See Barreto-Souza and Simas (2016) <doi:10.1007/s11222-015-9601-6> for further details.  
	"""
	
	homepage = "https://github.com/vpnsctl/mixpoissonreg/"
	cran = "mixpoissonreg" 

	version("1.0.0", md5="3b72ebb0d9da0e249f08368a52d6ec09")

	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
