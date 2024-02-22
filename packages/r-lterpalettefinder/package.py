# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLterpalettefinder(RPackage):
	"""Extract Color Palettes from Photos and Pick Official LTER
Palettes

	Allows identification of palettes derived from LTER (Long Term Ecological Research) 
   photographs based on user criteria.
   Also facilitates extraction of palettes from users' photos directly.
	"""
	
	cran = "lterpalettefinder" 

	version("1.1.0", md5="3eef4cab95398478dc7e365f3a4fd34d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
