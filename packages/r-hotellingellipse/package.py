# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHotellingellipse(RPackage):
	"""Hotelling T-Square and Confidence Ellipse

	Functions to compute the semi-axes lengths and coordinate points of Hotelling ellipse. Bro and Smilde (2014) <DOI:10.1039/c3ay41907j>. Brereton (2016) <DOI:10.1002/cem.2763>.
	"""
	
	homepage = "https://github.com/ChristianGoueguel/HotellingEllipse"
	cran = "HotellingEllipse" 

	version("1.1.0", md5="74eaeaa5cb08c02e6e5a4d17825f1a13")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
