# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetasurvival(RPackage):
	"""Meta-Analysis of a Single Survival Curve

	To assess a summary survival curve from survival probabilities and number of at-risk patients collected at various points in time in various studies, and to test the between-strata heterogeneity.
	"""
	
	homepage = "https://github.com/shubhrampandey/metaSurvival"
	cran = "metaSurvival" 

	version("0.1.0", md5="51288b7251c912620a7918ea40986b74")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
