# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicsim(RPackage):
	"""Performing Continuous-Time Microsimulation

	This toolkit allows performing continuous-time microsimulation for a wide range of life science (demography, social sciences, epidemiology) applications. Individual life-courses are specified by a continuous-time multi-state model as described in Zinn (2014) <doi:10.34196/IJM.00105>. 
	"""
	
	cran = "MicSim" 

	version("2.0.1", md5="5132f9a6e81981a1af40389132f7ddd7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-rlecuyer", type=("build", "run"))
