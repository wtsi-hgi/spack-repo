# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernhaz(RPackage):
	"""Kernel Estimation of Hazard Function in Survival Analysis

	Producing kernel estimates of the unconditional and conditional hazard
        function for right-censored data including methods of bandwidth selection.
	"""
	
	cran = "kernhaz" 

	version("0.1.0", md5="398dd0e34f8cd4363f4eeb8a5e82d6ee")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
