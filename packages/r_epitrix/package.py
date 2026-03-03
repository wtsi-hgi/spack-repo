# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitrix(RPackage):
	"""Small Helpers and Tricks for Epidemics Analysis

	A collection of small functions useful for epidemics analysis and infectious disease modelling. This includes computation of basic reproduction numbers from growth rates, generation of hashed labels to anonymize data, and fitting discretized Gamma distributions.
	"""
	
	homepage = "http://www.repidemicsconsortium.org/epitrix/"
	cran = "epitrix" 

	version("0.4.0", md5="900dde4d9f940cd2dfc81b8bf1ba22d1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
	depends_on("r-distcrete", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
