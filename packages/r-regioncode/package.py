# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegioncode(RPackage):
	"""Convert Region Names and Division Codes of China Over Years

	A fast tool to conquer the difficulties to convert various region names and administration division codes of Chinese regions. The current version enables seamlessly converting Chinese regions' formal names, common-used names, and codes between each other at the city level from 1986 to 2019.
	"""
	
	cran = "regioncode" 

	version("0.1.1", md5="5913b57544b6df959932b72438ec942a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pinyin", type=("build", "run"))
	depends_on("r-textshaping", type=("build", "run"))
