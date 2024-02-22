# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHac(RPackage):
	"""Estimation, Simulation and Visualization of Hierarchical
Archimedean Copulae (HAC)

	Package provides the estimation of the structure and the parameters, sampling methods and structural plots of Hierarchical Archimedean Copulae (HAC).
	"""
	
	homepage = "https://tu-dresden.de/bu/verkehr/ivw/osv/die-professur/inhaber-in"
	cran = "HAC" 

	version("1.1-0", md5="cbed71195d83bbf49276b25a564a552c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
