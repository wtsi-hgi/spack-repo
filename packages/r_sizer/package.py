# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSizer(RPackage):
	"""Significant Zero Crossings

	Calculates and plots the SiZer map for scatterplot data.  A 
  SiZer map is a way of examining when the p-th derivative of a 
  scatterplot-smoother is significantly negative, possibly zero or 
  significantly positive across a range of smoothing bandwidths.
	"""
	
	homepage = "https://github.com/dereksonderegger/SiZer"
	cran = "SiZer" 

	version("0.1-8", md5="41c13d1a971cdf568c13fc491d0f9f35")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
