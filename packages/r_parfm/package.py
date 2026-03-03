# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParfm(RPackage):
	"""Parametric Frailty Models

	Fits Parametric Frailty Models by maximum marginal likelihood.
             Possible baseline hazards:
                 exponential, Weibull, inverse Weibull (Fréchet),
                 Gompertz, lognormal, log-skew-normal, and loglogistic.
             Possible Frailty distributions:
                gamma, positive stable, inverse Gaussian and lognormal.
	"""
	
	cran = "parfm" 

	version("2.7.7", md5="f55ff4787c82496665ef17f019d3582c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
