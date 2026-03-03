# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgvar(RPackage):
	"""Bayesian Global Vector Autoregressions

	Estimation of Bayesian Global Vector Autoregressions (BGVAR) with different prior setups and the possibility to introduce stochastic volatility. Built-in priors include the Minnesota, the stochastic search variable selection and Normal-Gamma (NG) prior. For a reference see also Crespo Cuaresma, J., Feldkircher, M. and F. Huber (2016) "Forecasting with Global Vector Autoregressive Models: a Bayesian Approach", Journal of Applied Econometrics, Vol. 31(7), pp. 1371-1391 <doi:10.1002/jae.2504>. Post-processing functions allow for doing predictions, structurally identify the model with short-run or sign-restrictions and compute impulse response functions, historical decompositions and forecast error variance decompositions. Plotting functions are also available. The package has a companion paper: Boeck, M., Feldkircher, M. and F. Huber (2022) "BGVAR: Bayesian Global Vector Autoregressions with Shrinkage Priors in R", Journal of Statistical Software, Vol. 104(9), pp. 1-28 <doi:10.18637/jss.v104.i09>.
	"""
	
	homepage = "https://github.com/mboeck11/BGVAR"
	cran = "BGVAR" 

	version("2.5.5", md5="27b592bcb7cbee7e341271ab16cf18bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bayesm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stochvol", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
