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

	# R 4.5 compatibility requires R_* alloc macros
	version("0.15-4", sha256="4e9342f6fd65dc39c9dfed20cb0312d34899b9cb0648aa5a67516ce7711c20cf")
	version("0.15-2", sha256="8a67e22e3b2ee7a10ce26c1212cba763a272bd4327f9082fa70a382cd4a7c05d")
	version("0.15-0", sha256="8aa9d5daec455586fe6fab3db5b1bfa85d1157ff55af98d936bc654c20f33829")
	version("0.14-7", sha256="c01ed03509dee22b58b39da176a6427c2026efd901e9b0fb9f42ab022fd58716")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

	# Apply R 4.5 compatibility edits for legacy sources
	patch("r-transport-r45-compat.patch", when="@:0.15-2")
