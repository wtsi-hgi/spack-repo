# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REks(RPackage):
	"""Tidy and Geospatial Kernel Smoothing

	Extensions of the kernel smoothing functions from the 'ks' package for compatibility with the tidyverse and geospatial ecosystems <doi:10.48550/arXiv.2203.01686>.
	"""
	
	homepage = "https://www.mvstat.net/mvksa/"
	cran = "eks" 

	version("1.0.4", md5="f24c69194989debccd8b03e4e86c1cf2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mapsf", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
