# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSetrng(RPackage):
	"""Set (Normal) Random Number Generator and Seed

	Provides utilities to help set and record the setting of
	the seed and the uniform and normal generators used when a random
	experiment is run. The utilities can be used in other functions 
	that do random experiments to simplify recording and/or setting all the 
	necessary information for reproducibility. 
	See the vignette and reference manual for examples.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "setRNG" 

	version("2024.2-1", md5="0360795dcce8779f150ed6eefacf04b7")

	depends_on("r@2.5:", type=("build", "run"))
