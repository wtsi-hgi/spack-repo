# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReaddim(RPackage):
	"""Read ESA SNAP Processed Raster Format in R

	It helps you to read (.dim) images with CRS directly into R programming. One can import both Sentinel 1 and 2 images or any processed data with this software.
	"""
	
	cran = "ReadDIM" 

	version("0.2.11", md5="c215dd7235eeb48fb5e846db87075910")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
