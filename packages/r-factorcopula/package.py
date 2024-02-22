# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactorcopula(RPackage):
	"""Factor, Bi-Factor, Second-Order and Factor Tree Copula Models

	Estimation, model selection and goodness-of-fit of (1) factor copula models for mixed continuous and discrete data in Kadhem and Nikoloulopoulos (2021) <doi:10.1111/bmsp.12231>; (2) bi-factor and second-order copula models for item response data in Kadhem and Nikoloulopoulos (2023) <doi:10.1007/s11336-022-09894-2>; (3) factor tree copula models for item response data in Kadhem and Nikoloulopoulos (2022) <arXiv:2201.00339>.
	"""
	
	cran = "FactorCopula" 

	version("0.9.3", md5="cfea49f09d97de262e1180bb19afa71d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
