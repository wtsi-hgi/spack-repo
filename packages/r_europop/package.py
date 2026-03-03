# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REuropop(RPackage):
	"""Historical Populations of European Cities, 1500-1800

	This dataset contains population estimates of all European cities 
    with at least 10,000 inhabitants during the period 1500-1800. These data are
    adapted from Jan De Vries, "European Urbanization, 1500-1800" (1984).
	"""
	
	homepage = "https://github.com/mdlincoln/europop"
	cran = "europop" 

	version("0.3.1", md5="0c696a38b6ce1c3163c3a9b4b1c1ed47")

	depends_on("r@2.10:", type=("build", "run"))
