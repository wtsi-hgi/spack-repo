# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoinprofile(RPackage):
	"""Coincident Profile

	Builds the 
  coincident profile proposed by Martinez, W and Nieto, Fabio H and Poncela, P (2016) 
  <doi:10.1016/j.spl.2015.11.008>.
  This methodology studies the relationship between a couple of
  time series based on the the set of turning points of each
  time series. The coincident profile establishes if two time
  series are coincident, or one of them leads the second.
	"""
	
	homepage = "https://github.com/WilmerMartinezR/Coinprofile"
	cran = "Coinprofile" 

	version("0.1.9", md5="1c66568498313783fe0b222d0796d6da")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-exactranktests@0.8.29:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
