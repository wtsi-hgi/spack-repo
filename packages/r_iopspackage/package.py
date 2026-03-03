# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIopspackage(RPackage):
	"""IO-PS Framework Package

	A developmental R tool related to the input-output product space (IO-PS).
    The package requires two compulsory user inputs (raw CEPPI BACI trade data, and any acceptable ISO country code) and has 4 optional user inputs (a value chain map, chosen complexity method, number of iterations to be performed, and a trade digit level).
    Various metrics are calculated, such as Economic- and Product complexity, distance, opportunity gain, and inequality metrics, to facilitate better decision making regarding industrial policy making.
	"""
	
	cran = "iopspackage" 

	version("2.1.0", md5="625d60343fd015c1e7caa6556fbd22d9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-economiccomplexity", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
