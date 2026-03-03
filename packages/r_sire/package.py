# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSire(RPackage):
	"""Finding Feedback Effects in SEM and Testing for Their
Significance

	Provides two main functionalities.
    1 - Given a system of simultaneous equation,
    it decomposes  the matrix of coefficients weighting the endogenous variables 
    into three submatrices: one includes the subset of coefficients that have a causal nature
    in the model, two include the subset of coefficients that have a interdependent nature
    in the model, either at systematic level or induced by the correlation between error terms.
    2 - Given a decomposed model,
    it tests for the significance of the interdependent relationships acting in the system, 
    via Maximum likelihood and Wald test, which can be built starting from the function output.
    For theoretical reference see Faliva (1992) <doi:10.1007/BF02589085> and 
    Faliva and Zoia (1994) <doi:10.1007/BF02589041>.
	"""
	
	cran = "SIRE" 

	version("1.1.0", md5="c81343f97f23ab5e1610a6a7e5f7b321")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
