# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCholera(RPackage):
	"""Amend, Augment and Aid Analysis of John Snow's Cholera Map

	Amends errors, augments data and aids analysis of John Snow's map
  of the 1854 London cholera outbreak.
	"""
	
	homepage = "https://github.com/lindbrook/cholera"
	cran = "cholera" 

	version("0.8.0", md5="a8b8be31a277b3cece0938989662d246")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-deldir@1.0.2:", type=("build", "run"))
	depends_on("r-elevatr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-histdata@0.7.8:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tanaka", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-threejs", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
