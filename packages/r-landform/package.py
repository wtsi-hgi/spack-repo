# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandform(RPackage):
	"""Topographic Position Index-Based Landform Classification

	Provides a function for classifying a landscape into different categories based on the Topographic Position Index (TPI) and slope. It offers two types of classifications: Slope Position Classification, and Landform Classification. The function internally calculates the TPI for the given landscape and then uses it along with the slope to perform the classification. Optionally, descriptive statistics for every class are calculated and plotted. The classifications are useful for identifying the position of a location on a slope and for identifying broader landform types.
	"""
	
	cran = "landform" 

	version("0.2", md5="a4a9c35945bb5408f5667927012d3ca7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-terra@1.7:", type=("build", "run"))
