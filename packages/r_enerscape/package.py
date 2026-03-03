# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnerscape(RPackage):
	"""Compute Energy Landscapes

	Compute energy landscapes using a digital elevation model raster and body mass of animals.
	"""
	
	cran = "enerscape" 

	version("1.1.0", md5="37af8cfaf98678e79019a8b13a30f7d0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
