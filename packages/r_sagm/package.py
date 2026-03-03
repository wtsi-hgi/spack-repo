# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSagm(RPackage):
	"""Spatial Autoregressive Graphical Model

	Implements the methodological developments found in Hermes, van Heerwaarden, and Behrouzi (2023) <doi:10.48550/arXiv.2308.04325>, and allows for the statistical modeling of asymmetric between-location effects, as well as within-location effects using spatial autoregressive graphical models. The package allows for the generation of spatial weight matrices to capture asymmetric effects for strip-type intercropping designs, although it can handle any type of spatial data commonly found in other sciences.  
	"""
	
	cran = "SAGM" 

	version("1.0.0", md5="4d8f91a0505ec672f7afc972df6af498")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-fastmatrix", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
