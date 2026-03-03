# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupmz(RPackage):
	"""Detecting Structural Change with Heteroskedasticity

	Calculates the sup MZ value to detect the unknown structural break points under Heteroskedasticity as given in Ahmed et al. (2017) (<DOI: 10.1080/03610926.2016.1235200>).
	"""
	
	homepage = "https://github.com/myaseen208/SupMZ"
	cran = "SupMZ" 

	version("0.2.0", md5="408ef8a1002f2b1c529aa73a5862b271")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
