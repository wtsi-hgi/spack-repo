# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpa(RPackage):
	"""Distributions Hermite Polynomial Approximation

	Multivariate conditional and marginal densities, moments, cumulative distribution functions as well as binary choice and sample selection models based on Hermite polynomial approximation which was proposed and described by A. Gallant and D. W. Nychka (1987) <doi:10.2307/1913241>.
	"""
	
	cran = "hpa" 

	version("1.3.3", md5="8384e05ffc1fd2b702b32305544b9332")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
