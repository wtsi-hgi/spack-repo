# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmfanova(RPackage):
	"""Repeated Measures Functional Analysis of Variance

	The provided package implements the statistical tests for the functional repeated measures analysis problem (Kurylo and Smaga, 2023, <arXiv:2306.03883>). These procedures enable us to verify the overall hypothesis regarding equality, as well as hypotheses for pairwise comparisons (i.e., post hoc analysis) of mean functions corresponding to repeated experiments.
	"""
	
	cran = "rmfanova" 

	version("0.1.0", md5="626d214cd91357fb609bbc51544ced31")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-refund", type=("build", "run"))
