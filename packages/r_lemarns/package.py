# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLemarns(RPackage):
	"""Length-Based Multispecies Analysis by Numerical Simulation

	Set up, run and explore the outputs of the Length-based Multi-species model (LeMans; Hall et al. 2006 <doi:10.1139/f06-039>), focused on the marine environment.
	"""
	
	cran = "LeMaRns" 

	version("0.1.2", md5="551eac9ad6c007229114aae006a26616")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
