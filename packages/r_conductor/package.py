# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConductor(RPackage):
	"""Create Tours in 'Shiny' Apps Using 'Shepherd.js'

	Enable the use of 'Shepherd.js' to create tours in 'Shiny' 
    applications.
	"""
	
	homepage = "https://github.com/etiennebacher/conductor"
	cran = "conductor" 

	version("0.1.1", md5="e78932c3ec53b29362e9743582cc2426")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
