# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcopula(RPackage):
	"""Hierarchical Archimedean Copulas Constructed with Multivariate
Compound Distributions

	Construct and manipulate hierarchical Archimedean copulas with multivariate compound distributions. The model used is the one of Cossette et al. (2017) <doi:10.1016/j.insmatheco.2017.06.001>. 
	"""
	
	cran = "nCopula" 

	version("0.1.1", md5="43de052d25c4a9ad6a352607d4897085")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
