# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsdm(RPackage):
	"""Uncertainty Analysis for Species Distribution Models

	This is a framework that aims to provide methods and tools for assessing the impact of different sources of uncertainties (e.g.positional uncertainty) on performance of species distribution models (SDMs).)
	"""
	
	homepage = "https://r-gis.net/"
	cran = "usdm" 

	version("2.1-7", md5="eeebcd4bcf42ef8f8bf011eada34b336")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
