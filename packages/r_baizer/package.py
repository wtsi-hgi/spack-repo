# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaizer(RPackage):
	"""Useful Functions for Data Processing

	In ancient Chinese mythology, Bai Ze is a divine creature that knows the needs of everything.
    'baizer' provides data processing functions frequently used by the author.
    Hope this package also knows what you want!
	"""
	
	homepage = "https://william-swl.github.io/baizer/"
	cran = "baizer" 

	version("0.8.0", md5="a4688552def6f8d10b3419997cd1de23")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-diffobj", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
