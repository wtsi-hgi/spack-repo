# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpdep(RPackage):
	"""Spatial Dependence: Weighting Schemes, Statistics.

	A collection of functions to create spatial weights matrix objects from
	polygon 'contiguities', from point patterns by distance and tessellations,
	for summarizing these objects, and for permitting their use in spatial data
	analysis, including regional aggregation by minimum spanning tree; a
	collection of tests for spatial 'autocorrelation', including global 'Morans
	I' and 'Gearys C' proposed by 'Cliff' and 'Ord' (1973, ISBN: 0850860369)
	and (1981, ISBN: 0850860814), 'Hubert/Mantel' general cross product
	statistic, Empirical Bayes estimates and 'Assuncao/Reis' (1999)
	<doi:10.1002/(SICI)1097-0258(19990830)18:16%3C2147::AID-SIM179%3E3.0.CO"""

	cran = "spdep"

	license("GPL-2.0-or-later")

	version("1.3-3", md5="cff3e87a727adbd95b588455bba53a38")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-spdata@0.2.6:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-boot@1.3.1:", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-s2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-sp@1:", type=("build", "run"))
