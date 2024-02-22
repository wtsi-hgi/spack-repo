# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcirt(RPackage):
	"""Forced Choice in Item Response Theory

	Bayesian estimation of forced choice models in Item Response Theory using 'rstan' (See Stan Development Team (2020) <https://mc-stan.org/>).
	"""
	
	homepage = "https://github.com/Naidantu/fcirt"
	cran = "fcirt" 

	version("0.1.0", md5="0752befdd3b408b3600b0a0438dd1770")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
