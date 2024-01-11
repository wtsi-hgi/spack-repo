# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RPaletteer(RPackage):
	"""Comprehensive Collection of Color Palettes

	The choices of color palettes in R can be quite
    overwhelming with palettes spread over many packages with many
    different API's. This packages aims to collect all color palettes
    across the R ecosystem under the same package with a streamlined API.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/paletteer"
	cran = "paletteer" 

	version("1.5.0", md5="b4814df17b6c67809d2f3cfd9333ee08")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-prismatic", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
