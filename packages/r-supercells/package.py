# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupercells(RPackage):
	"""Superpixels of Spatial Data

	Creates superpixels based on input spatial data. 
  This package works on spatial data with one variable (e.g., continuous raster), many variables (e.g., RGB rasters), and spatial patterns (e.g., areas in categorical rasters).
  It is based on the SLIC algorithm (Achanta et al. (2012) <doi:10.1109/TPAMI.2012.120>), and readapts it to work with arbitrary dissimilarity measures. 
	"""
	
	homepage = "https://jakubnowosad.com/supercells/"
	cran = "supercells" 

	version("1.0.0", md5="22180e8ddf3bc1e6ba714c86546e36f5")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra@1.4.21:", type=("build", "run"))
	depends_on("r-philentropy@0.6:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
