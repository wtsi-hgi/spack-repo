# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPendensity(RPackage):
	"""Density Estimation with a Penalized Mixture Approach

	Estimation of univariate (conditional) densities using penalized B-splines with automatic selection of optimal smoothing parameter.
	"""
	
	cran = "pendensity" 

	version("0.2.13", md5="483796679aa84dc6f3d4d53898c7ca2a")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
