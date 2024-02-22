# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoresim(RPackage):
	"""Core Functionality for Simulating Quantities of Interest from
Generalised Linear Models

	Core functions for simulating quantities of interest
    from generalised linear models (GLM). This package will form the backbone of
    a series of other packages that improve the interpretation of GLM estimates.
	"""
	
	cran = "coreSim" 

	version("0.2.4", md5="1c40376914ed7602205f88e73194a554")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
