# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyrates(RPackage):
	"""Tidy Epidemiological Rates

	Compute age-adjusted rates by direct and indirect methods and other epidemiological indicators in a tidy way, wrapping functions from the 'epitools' package.
	"""
	
	homepage = "https://rfsaldanha.github.io/tidyrates/"
	cran = "tidyrates" 

	version("0.0.1", md5="dfae7841625bbc381f2a3b02e18c12bf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
