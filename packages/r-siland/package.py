# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiland(RPackage):
	"""Spatial Influence of Landscape

	Method to estimate the spatial influence scales of landscape variables on a response variable. The method is based on Chandler and Hepinstall-Cymerman (2016) Estimating the spatial scales of landscape effects on abundance, Landscape ecology, 31: 1383-1394, <doi:10.1007/s10980-016-0380-z>.
	"""
	
	cran = "siland" 

	version("3.0.2", md5="14b5b09f062ca001f96de15b8d8de38b")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-fasterize", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
