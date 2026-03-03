# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJoinerml(RPackage):
	"""Joint Modelling of Multivariate Longitudinal Data and
Time-to-Event Outcomes

	Fits the joint model proposed by Henderson and colleagues (2000) 
    <doi:10.1093/biostatistics/1.4.465>, but extended to the case of multiple 
    continuous longitudinal measures. The time-to-event data is modelled using a 
    Cox proportional hazards regression model with time-varying covariates. The 
    multiple longitudinal outcomes are modelled using a multivariate version of the 
    Laird and Ware linear mixed model. The association is captured by a multivariate
    latent Gaussian process. The model is estimated using a Monte Carlo Expectation 
    Maximization algorithm. This project was funded by the Medical Research Council 
    (Grant number MR/M013227/1).
	"""
	
	homepage = "https://github.com/graemeleehickey/joineRML"
	cran = "joineRML" 

	version("0.4.6", md5="7070d6e1f4b0abd733456f19205791e6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4@1.1.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
