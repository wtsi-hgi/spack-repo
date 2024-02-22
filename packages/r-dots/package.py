# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDots(RPackage):
	"""Dot Density Maps

	Generate point data for representing people within spatial data. This
  collects a suite of tools for creating simple dot density maps. Several functions 
  from different spatial packages are standardized to take the same arguments so
  that they can be easily substituted for each other.
	"""
	
	homepage = "https://github.com/christopherkenny/dots"
	cran = "dots" 

	version("0.0.2", md5="4287f0aa3adea2dab094593bfea0ee89")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
