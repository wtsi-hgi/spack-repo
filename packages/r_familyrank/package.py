# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamilyrank(RPackage):
	"""Algorithm for Ranking Predictors Using Graphical Domain
Knowledge

	Grows families of features by selecting features that maximize a weighted score calculated from empirical feature scores and graphical knowledge. The final weighted score for a feature is determined by summing a feature's family-weighted scores across all families in which the feature appears.
	"""
	
	cran = "FamilyRank" 

	version("1.0", md5="b9731110d2138de1538544d2432ff2b2")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
