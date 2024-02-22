# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmortalityplus(RPackage):
	"""Bayesian Mortality Modelling

	Fit Bayesian graduation mortality using the Heligman-Pollard model, as seen in Heligman, L., & Pollard, J. H. (1980) <doi:10.1017/S0020268100040257> and Dellaportas, Petros, et al. (2001) <doi:10.1111/1467-985X.00202>, and dynamic linear model (Campagnoli, P., Petris, G., and Petrone, S. (2009) <doi:10.1007/b135794_2>). While Heligman-Pollard has parameters with a straightforward interpretation yielding some rich analysis, the dynamic linear model provides a very flexible adjustment of the mortality curves by controlling the discount factor value. Closing methods for both Heligman-Pollard and dynamic linear model were also implemented according to Dodd, Erengul, et al. (2018) <https://www.jstor.org/stable/48547511>. The Bayesian Lee-Carter model is also implemented to fit historical mortality tables time series to predict the mortality in the following years and to do improvement analysis, as seen in Lee, R. D., & Carter, L. R. (1992) <doi:10.1080/01621459.1992.10475265> and Pedroza, C. (2006) <doi:10.1093/biostatistics/kxj024>.
	"""
	
	cran = "BayesMortalityPlus" 

	version("0.2.2", md5="5e0c438631fc083eca8eeecc68102b79")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
