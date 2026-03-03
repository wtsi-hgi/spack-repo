# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevealedprefs(RPackage):
	"""Revealed Preferences and Microeconomic Rationality

	Computation of (direct and indirect) revealed preferences, fast non-parametric tests of rationality axioms (WARP, SARP, GARP), simulation of axiom-consistent data, and detection of axiom-consistent subpopulations. Rationality tests follow Varian (1982) <doi:10.2307/1912771>, axiom-consistent subpopulations follow Crawford and Pendakur (2012) <doi:10.1111/j.1468-0297.2012.02545.x>.
	"""
	
	cran = "revealedPrefs" 

	version("0.4.1", md5="fd87f32760cab7eca10a3a81890a783e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
