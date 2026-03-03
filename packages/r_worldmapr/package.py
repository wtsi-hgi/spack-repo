# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorldmapr(RPackage):
	"""Worldwide or Coordinates-Based Heat Maps

	Easily plot heat maps of the world, based on continuous or categorical data. Country labels can also be added to the map. 
	"""
	
	homepage = "https://github.com/Luigi-Annic/WorldMapR/"
	cran = "WorldMapR" 

	version("0.1.0", md5="96f438ef681ee8a2e002c376f13371d1")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-rnaturalearth@1.0.1:", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
	depends_on("r-countrycode@1.5:", type=("build", "run"))
