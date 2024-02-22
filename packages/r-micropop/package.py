# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicropop(RPackage):
	"""Process-Based Modelling of Microbial Populations

	Modelling interacting microbial populations - example applications
    include human gut microbiota, rumen microbiota and phytoplankton. Solves a
    system of ordinary differential equations to simulate microbial growth and
    resource uptake over time. This version contains network visualisation functions.
	"""
	
	homepage = "https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.12873"
	cran = "microPop" 

	version("1.6", md5="6cdff11bbb35b3f4f4f0a4b4a47073d7")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
