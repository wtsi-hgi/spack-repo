# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgaussian(RPackage):
	"""The q-Gaussian Distribution

	Density, distribution function, quantile function and 
  random generation for the q-gaussian distribution with parameters mu and sig.
	"""
	
	cran = "qGaussian" 

	version("0.1.8", md5="7d5119e327ad1cc8ef794183fb891101")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
