# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmvtnorm(RPackage):
	"""Truncated Multivariate Normal and Student t Distribution

	Random number generation for the truncated multivariate normal and Student t distribution. 
  Computes probabilities, quantiles and densities, 
  including one-dimensional and bivariate marginal densities. Computes first and second moments (i.e. mean and covariance matrix) for the double-truncated multinormal case.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "tmvtnorm" 

	version("1.6", md5="26c71b49d317622cd6b3d392b287115e")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gmm", type=("build", "run"))
