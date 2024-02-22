# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlux(RPackage):
	"""Flux Rate Calculation from Dynamic Closed Chamber Measurements

	Functions for the calculation of greenhouse gas flux rates 
	from closed chamber concentration measurements. The package follows 
	a modular concept: Fluxes can be calculated in just two simple steps 
	or in several steps if more control in details is wanted. Additionally 
	plot and preparation functions as well as functions for modelling
	gpp and reco are provided.
	"""
	
	cran = "flux" 

	version("0.3-0.1", md5="b433aeba39147224e3edde1bba2ca072")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
