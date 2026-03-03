# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGasanalyzer(RPackage):
	"""Import, Recompute and Analyze Data from Portable Gas Analyzers

	Provides functions to import data from several instruments
    commonly used by plant physiologists to measure characteristics
    related to photosynthesis. It provides a standardized list of variable
    names, and several sets of equations to calculate additional variables
    based on the measurements.  These equations have been described by von
    Caemmerer and Farquhar (1981) <doi:10.1007/BF00384257>, Busch et al.
    (2020) <doi:10.1038/s41477-020-0606-6> and Márquez et al. (2021)
    <doi:10.1038/s41477-021-00861-w>. In addition, this package
    facilitates performing sensitivity analyses on variables or
    assumptions used in the calculations.
	"""
	
	homepage = "https://gitlab.com/plantphys/gasanalyzer"
	cran = "gasanalyzer" 

	version("0.3.4", md5="86d43d3c5fc9f18e397e9a1bdb522a57")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-jsonify", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyxl@1.0.8:", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
