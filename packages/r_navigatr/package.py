# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNavigatr(RPackage):
	"""Navigation Menu for Pipe-Friendly Data Processing

	Provides a navigation menu to enable pipe-friendly data processing for hierarchical data structures.
    By activating the menu items, you can perform operations on each item while maintaining the overall structure in attributes.
	"""
	
	homepage = "https://github.com/UchidaMizuki/navigatr"
	cran = "navigatr" 

	version("0.2.1", md5="780e574492952b8dbd8b7ce2f07a83d3")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stickyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
