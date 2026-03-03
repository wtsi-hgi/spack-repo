# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuvicp(RPackage):
	"""MultiClass Visualizable Classification using Combination of
Projections

	An ensemble classifier for multiclass classification. This is a novel classifier that natively works as an ensemble. It projects data on a large number of matrices, and uses very simple classifiers on each of these projections. The results are then combined, ideally via Dempster-Shafer Calculus.
	"""
	
	cran = "MuViCP" 

	version("1.3.2", md5="0605a865443d5df3601327091ab74c97")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
