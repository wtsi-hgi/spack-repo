# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWindac(RPackage):
	"""Area Correction Methods

	Post-construction fatality monitoring studies at wind facilities are based on data from searches for bird and bat carcasses in plots beneath turbines. Bird and bat carcasses can fall outside of the search plot. Bird and bat carcasses from wind turbines often fall outside of the searched area. To compensate, area correction (AC) estimations are calculated to estimate the percentage of fatalities that fall within the searched area versus those that fall outside of it. This package provides two likelihood based methods and one physics based method (Hull and Muir (2010) <doi:10.1080/14486563.2010.9725253>, Huso and Dalthorp (2014) <doi:10.1002/jwmg.663>) to estimate the carcass fall distribution. There are also functions for calculating the proportion of area searched within one unit annuli, log logistic distribution functions, and truncated distribution functions.
	"""
	
	cran = "windAC" 

	version("1.2.10", md5="fe434c5932ff9364773d9ed8bf262ac3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
