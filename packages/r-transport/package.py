# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransport(RPackage):
	"""Computation of Optimal Transport Plans and Wasserstein Distances

	Solve optimal transport problems. Compute Wasserstein distances (a.k.a. Kantorovitch, Fortet--Mourier, Mallows, Earth Mover's, or minimal L_p distances), return the corresponding transference plans, and display them graphically. Objects that can be compared include grey-scale images, (weighted) point patterns, and mass vectors.
	"""
	
	homepage = "https://dschuhm1.pages.gwdg.de/software"
	cran = "transport" 

	version("0.15-0", md5="e2c2d35aeef8e940b30c6b4e270363da")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
