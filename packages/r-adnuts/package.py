# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdnuts(RPackage):
	"""No-U-Turn MCMC Sampling for 'ADMB' Models

	Bayesian inference using the no-U-turn (NUTS) algorithm by 
 Hoffman and Gelman (2014) <https://www.jmlr.org/papers/v15/hoffman14a.html>. 
 Designed for 'AD Model Builder' ('ADMB') models,
 or when R functions for log-density and log-density gradient
 are available, such as 'Template Model Builder'
 models and other special cases. Functionality is similar to 'Stan', 
 and the 'rstan' and 'shinystan' packages are used for diagnostics and 
 inference.
	"""
	
	homepage = "https://github.com/Cole-Monnahan-NOAA/adnuts"
	cran = "adnuts" 

	version("1.1.2", md5="b3c86166a696587294f72ae450e4006b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-snowfall@1.84.6.1:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-r2admb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
