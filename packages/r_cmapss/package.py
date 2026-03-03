# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmapss(RPackage):
	"""Commercial Modular Aero-Propulsion System Simulation Data Set

	Contains the Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) data set. 
	"""
	
	cran = "CMAPSS" 

	version("0.1.1", md5="8d7718b3e3be99366597308e16d321ab")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
