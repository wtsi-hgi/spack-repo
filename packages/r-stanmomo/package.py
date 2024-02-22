# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStanmomo(RPackage):
	"""Bayesian Mortality Modelling with 'Stan'

	Implementation of popular mortality models using the 'rstan' 
    package, which provides the R interface to the 'Stan' C++ library for 
    Bayesian estimation. The package supports well-known models proposed in the 
    actuarial and demographic literature including the Lee-Carter (1992) 
    <doi:10.1080/01621459.1992.10475265> and the Cairns-Blake-Dowd (2006) 
    <doi:10.1111/j.1539-6975.2006.00195.x> models. By a simple call, the user 
    inputs deaths and exposures and the package outputs the MCMC simulations for
    each parameter, the log likelihoods and predictions. Moreover, the package 
    includes tools for model selection and Bayesian model averaging by leave 
    future-out validation.
	"""
	
	homepage = "https://github.com/kabarigou/StanMoMo"
	cran = "StanMoMo" 

	version("1.2.0", md5="9a8f905450e43789a594bebd65c08b4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-bridgesampling", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
