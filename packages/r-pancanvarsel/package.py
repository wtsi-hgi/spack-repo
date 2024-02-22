# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPancanvarsel(RPackage):
	"""Pan-Cancer Variable Selection

	Provides function for performing Bayesian survival regression using 
    Horseshoe prior in the accelerated failure time model with log normal assumption 
    in order to achieve high dimensional pan-cancer variable selection as developed in
    Maity et. al. (2019) <doi:10.1111/biom.13132>.
	"""
	
	cran = "PanCanVarSel" 

	version("0.0.3", md5="826350cc3e8c4ca5137e63eea9924914")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-smoothmest", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
