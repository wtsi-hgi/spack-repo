# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzylp(RPackage):
	"""Fuzzy Linear Programming

	Provides methods to solve Fuzzy Linear Programming Problems with
             fuzzy constraints (following different approaches proposed by 
             Verdegay, Zimmermann, Werners and Tanaka), fuzzy costs, and fuzzy
             technological matrix. 
	"""
	
	homepage = "https://github.com/olbapjose/FuzzyLP"
	cran = "FuzzyLP" 

	version("0.1-7", md5="44b9a974d53298254e60f655baf3940b")

	depends_on("r-roi", type=("build", "run"))
	depends_on("r-fuzzynumbers", type=("build", "run"))
	depends_on("r-roi-plugin-glpk", type=("build", "run"))
