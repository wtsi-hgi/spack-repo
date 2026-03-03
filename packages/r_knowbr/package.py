# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnowbr(RPackage):
	"""Discriminating Well Surveyed Spatial Units from Exhaustive
Biodiversity Databases

	It uses species accumulation curves and diverse estimators to assess, at the same time, the levels of survey coverage in multiple geographic cells of a size defined by the user or polygons. It also enables the geographical depiction of observed species richness, survey effort and completeness values including a background with administrative areas.
	"""
	
	cran = "KnowBR" 

	version("2.2", md5="577a08bc3da5b0aa38d2fd2778022ad5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fossil", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
