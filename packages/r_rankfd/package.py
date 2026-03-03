# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankfd(RPackage):
	"""Rank-Based Tests for General Factorial Designs

	The rankFD() function calculates the Wald-type statistic (WTS) and the ANOVA-type
	     statistic (ATS) for nonparametric factorial designs, e.g., for count, ordinal or score data
	     in a crossed design with an arbitrary number of factors.
	     Brunner, E., Bathke, A. and Konietschke, F. (2018) <doi:10.1007/978-3-030-02914-2>.
	"""
	
	cran = "rankFD" 

	version("0.1.1", md5="c641c9a38035c1e0b0b1445f5207dacb")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-lattice@0.20.33:", type=("build", "run"))
	depends_on("r-mass@7.3.43:", type=("build", "run"))
	depends_on("r-coin@1.1.2:", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
