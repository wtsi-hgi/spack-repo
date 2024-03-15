# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNvmix(RPackage):
	"""Multivariate Normal Variance Mixtures

	Functions for working with (grouped) multivariate normal variance mixture
  distributions (evaluation of distribution functions and densities,
  random number generation and parameter estimation), including
  Student's t distribution for non-integer degrees-of-freedom as well as the grouped t
  distribution and copula with multiple degrees-of-freedom parameters.
  See <doi:10.18637/jss.v102.i02> for a high-level description of select functionality.
	"""
	
	cran = "nvmix" 

	version("0.1-1", md5="14ba1fe80fff780dc7ffb4248e0793cb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-qrng", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
