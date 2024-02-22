# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlreg(RPackage):
	"""Power Logit Regression for Modeling Bounded Data

	Power logit regression models for bounded
  continuous data, in which the density generator may be normal, Student-t, 
  power exponential, slash, hyperbolic, sinh-normal, or type II logistic. 
  Diagnostic tools associated with the fitted model, such as the residuals, 
  local influence measures, leverage measures, and goodness-of-fit statistics,
  are implemented. The estimation process follows the maximum likelihood approach
  and, currently, the package supports two types of estimators: the usual maximum 
  likelihood estimator and the penalized maximum likelihood estimator. More details
  about power logit regression models are described in 
  Queiroz and Ferrari (2022) <arXiv:2202.01697>.
	"""
	
	homepage = "https://github.com/ffqueiroz/PLreg"
	cran = "PLreg" 

	version("0.4.1", md5="f86a098b767adebb792c68f05ee18cd6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-generalizedhyperbolic", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
