# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpind(RPackage):
	"""Spatial Methods and Indices

	Functions for spatial methods based on generalized estimating equations (GEE) and
  wavelet-revised methods (WRM), functions for scaling by wavelet multiresolution regression (WMRR),
  conducting multi-model inference, and stepwise model selection. Further, contains functions 
  for spatially corrected model accuracy measures.
	"""
	
	homepage = "https://github.com/levisc8/spind"
	cran = "spind" 

	version("2.2.1", md5="736c553702ca4468f15c783e2743e91d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gee@4.13.19:", type=("build", "run"))
	depends_on("r-geepack@1.2.1:", type=("build", "run"))
	depends_on("r-mass@7.3.49:", type=("build", "run"))
	depends_on("r-splancs@2.1.40:", type=("build", "run"))
	depends_on("r-lattice@0.20.35:", type=("build", "run"))
	depends_on("r-waveslim@1.7.5:", type=("build", "run"))
	depends_on("r-rje@1.9:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-rlang@0.2.1:", type=("build", "run"))
