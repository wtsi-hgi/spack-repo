# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgbp(RPackage):
	"""Hierarchical Modeling and Frequency Method Checking on
Overdispersed Gaussian, Poisson, and Binomial Data

	We utilize  approximate Bayesian machinery to fit two-level conjugate hierarchical models on overdispersed Gaussian, Poisson, and Binomial data and evaluates whether the resulting approximate Bayesian interval estimates for random effects meet the nominal confidence levels via frequency coverage evaluation. The data that Rgbp assumes comprise observed sufficient statistic for each random effect, such as an average or a proportion of each group, without population-level data.  The approximate Bayesian tool equipped with the adjustment for density maximization produces approximate point and interval estimates for model parameters including second-level variance component, regression coefficients, and random effect. For the Binomial data, the package provides an option to produce  posterior samples of all the model parameters via the acceptance-rejection method. The package provides a quick way to evaluate coverage rates of the resultant Bayesian interval estimates for random effects via a parametric bootstrapping, which we call frequency method checking.
	"""
	
	cran = "Rgbp" 

	version("1.1.4", md5="c612184c814bb6a2e191df607a749d65")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
