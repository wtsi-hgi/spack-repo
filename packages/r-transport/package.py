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

	version("0.14-7", md5="b33b68547bf84921b3824b0e1d0af30a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
