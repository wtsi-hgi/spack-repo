# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLadderfuelsr(RPackage):
	"""Automated Tool for Vertical Fuel Continuity Analysis using
Airborne Laser Scanning Data

	Set of tools for analyzing vertical fuel continuity at the tree level using Airborne Laser Scanning data. The workflow consisted of: 1) calculating the vertical height profiles of each segmented tree; 2) identifying gaps and fuel layers; 3) estimating the distance between fuel layers; and 4) retrieving the fuel layers base height and depth. Additionally, other functions recalculate previous metrics after considering distances greater than 1 m and calculate the canopy base height as the fuel base height located at the largest- and at the last-distance. Moreover, the package calculates: i) the percentage of Leaf Area Density comprised in each fuel layer, ii) remove fuel layers with Leaf Area Density percentage less than 25, iii) recalculate the distances among the reminder ones, and iv) identify the canopy base height as the fuel base height with the highest Leaf Area Density percentage. On the other hand, when there is only one fuel layer, it identifies the canopy base height performing a segmented linear regression (breaking points) on the cumulative sum of Leaf Area Density as a function of height. Finally, a collection of plotting functions is developed to represent: i) the initial gaps and fuel layers; ii) the fuels base height, depths and gaps with distances greater than 1 m and, iii) the fuels base height and depths after applying the breaking point method over trees with only one fuel layer. The methods implemented in this package are original and have not been published elsewhere.
	"""
	
	homepage = "https://github.com/olgaviedma/LadderFuelsR"
	cran = "LadderFuelsR" 

	version("0.0.3", md5="58bacb820f4961d638bab42ca40ef8a3")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
