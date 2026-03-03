# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmc(RPackage):
	"""Kaplan-Meier Estimator with Constraints for Right Censored Data
-- a Recursive Computational Algorithm

	Given constraints for right censored data, we use a recursive computational algorithm to calculate the the "constrained" Kaplan-Meier estimator. The constraint is assumed given in linear estimating equations or mean functions. We also illustrate how this leads to the empirical likelihood ratio test with right censored data and accelerated failure time model with given coefficients. EM algorithm from emplik package is used to get the initial value. The properties and performance of the EM algorithm is discussed in Mai Zhou and Yifan Yang (2015)<doi: 10.1007/s00180-015-0567-9> and Mai Zhou and Yifan Yang (2017) <doi: 10.1002/wics.1400>. More applications could be found in Mai Zhou (2015) <doi: 10.1201/b18598>.
	"""
	
	homepage = "https://github.com/yfyang86/kmc/"
	cran = "kmc" 

	version("0.4-2", md5="919a4d9db86b54ee58fd2af006b1c413")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-emplik", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
