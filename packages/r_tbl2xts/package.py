# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbl2xts(RPackage):
	"""Convert Tibbles or Data Frames to Xts Easily

	Facilitate the movement between data frames to 'xts'. Particularly
    useful when moving from 'tidyverse' to the widely used 'xts' package, which is
    the input format of choice to various other packages. It also allows the user 
    to use a 'spread_by' argument for a character column 'xts' conversion.
	"""
	
	homepage = "https://tbl2xts.nfkatzke.com"
	cran = "tbl2xts" 

	version("1.0.4", md5="d1d6e1eb2555501383d61f6930e5b628")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
