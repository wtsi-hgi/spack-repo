# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColornamer(RPackage):
	"""Give Colors a Name

	A tool for transforming coordinates in a color space to common
    color names using data from the Royal Horticultural Society and the
    International Union for the Protection of New Varieties of Plants.
	"""
	
	homepage = "https://github.com/msanchez-beeckman/ColorNameR"
	cran = "ColorNameR" 

	version("0.1.0", md5="7de3d4e7f74cdac04bdbe3b6adb666d4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
