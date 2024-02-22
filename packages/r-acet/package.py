# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcet(RPackage):
	"""Estimating Dynamic Heritability and Twin Model Comparison

	Twin models that are able to estimate the dynamic behaviour of the variance components in the classical twin models with respect to age using B-splines and P-splines.
	"""
	
	cran = "ACEt" 

	version("1.9.0", md5="ed656bf593d3d7ee7c01f11c9be6ed81")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
