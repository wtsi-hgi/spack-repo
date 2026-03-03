# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcaod(RPackage):
	"""Optimal Designs for Nonlinear Statistical Models by Imperialist
Competitive Algorithm (ICA)

	Finds optimal designs for nonlinear models using a metaheuristic algorithm called Imperialist Competitive Algorithm (ICA). See, for details, Masoudi et al. (2017) <doi:10.1016/j.csda.2016.06.014> and Masoudi et al. (2019) <doi:10.1080/10618600.2019.1601097>.
	"""
	
	cran = "ICAOD" 

	version("1.0.1", md5="d0c264722bdbd215b1443bfc24fe1a3d")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mvquad", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
