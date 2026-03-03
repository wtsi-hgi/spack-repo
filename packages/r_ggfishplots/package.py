# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfishplots(RPackage):
	"""Visualise and Calculate Life History Parameters for Fisheries
Science using 'ggplot2'

	Contains functions to create life history parameter plots from raw data. 
	The plots are created using 'ggplot2', and calculations done using the 'tidyverse'
	collection of packages. The package contains references to FishBase 
	(Froese R., Pauly. D., 2023) <https://www.fishbase.se/>.
	"""
	
	homepage = "https://github.com/DeepWaterIMR/ggFishPlots"
	cran = "ggFishPlots" 

	version("0.2.2", md5="9e72d4dc37ad0aabacd57caa5dca35b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-fishmethods", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
