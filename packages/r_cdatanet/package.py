# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdatanet(RPackage):
	"""Modeling Count Data with Peer Effects

	Likelihood-based estimation and data generation from a class of models used to estimate peer effects on count data by controlling for the network endogeneity. This class includes count data models with social interactions (Houndetoungan 2023; <doi:10.2139/ssrn.3721250>), spatial tobit models (Xu and Lee 2015; <doi:10.1016/j.jeconom.2015.05.004>), and spatial linear-in-means models (Lee 2004; <doi:10.1111/j.1468-0262.2004.00558.x>).  
	"""
	
	homepage = "https://github.com/ahoundetoungan/CDatanet"
	cran = "CDatanet" 

	version("2.1.3", md5="524b738dc57d5c355b4323b8ba178235")
	version("2.1.2", md5="12c9a6be63328f5279c083c7a2c8bf39")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-ddpcr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
