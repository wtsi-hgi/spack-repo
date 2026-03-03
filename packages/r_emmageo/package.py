# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmmageo(RPackage):
	"""End-Member Modelling of Grain-Size Data

	End-member modelling analysis of grain-size data is an approach 
    to unmix a data set's underlying distributions and their contribution to 
    the data set. EMMAgeo provides deterministic and robust protocols for 
    that purpose. 
	"""
	
	cran = "EMMAgeo" 

	version("0.9.7", md5="664ba62396de2037d12df18312ea516c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
