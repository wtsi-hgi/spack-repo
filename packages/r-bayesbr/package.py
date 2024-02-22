# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesbr(RPackage):
	"""Beta Regression on a Bayesian Model

	Applies the Beta regression model in the Bayesian statistical view with the possibility of adding a spatial effect in the parameters, the Beta regression is used when the response variable is a proportion variable, that is, it only accepts values between 0 and 1.
    The package 'bayesbr' uses 'rstan' package to build the Bayesian statistical models. The main function of the package receives as a parameter a form informing the independent variable and the co-variables of the model to be made, as output it returns a list with the results of the model. For more details see Ferrari and Cribari-Neto (2004) <doi:10.1080/0266476042000214501> and Hoffman and Gelman (2014) <arXiv:1111.4246>.
	"""
	
	homepage = "https://github.com/pjoao266/bayesbr"
	cran = "bayesbr" 

	version("0.0.1.0", md5="daa824cd6ef22ca169f91be54bb67860")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fdrtool@1.2.15:", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-loo@2.2:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
