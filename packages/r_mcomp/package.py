# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcomp(RPackage):
	"""Data from the M-Competitions

	
  The 1001 time series from the M-competition (Makridakis et al. 1982) <DOI:10.1002/for.3980010202> and the 3003 time series from the IJF-M3 competition (Makridakis and Hibon, 2000) <DOI:10.1016/S0169-2070(00)00057-1>.
	"""
	
	homepage = "http://pkg.robjhyndman.com/Mcomp/"
	cran = "Mcomp" 

	version("2.8", md5="9003bd75eb8a07199dc9e95890ed8b6a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast@8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
