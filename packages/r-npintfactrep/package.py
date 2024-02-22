# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpintfactrep(RPackage):
	"""Nonparametric Interaction Tests for Factorial Designs with
Repeated Measures

	Returns nonparametric aligned rank tests for the interaction in two-way factorial designs, on R data sets with repeated measures in 'wide' format. Five ANOVAs tables are reported. A PARAMETRIC one on the original data, one for a CHECK upon the interaction alignments, and three aligned rank tests: one on the aligned REGULAR, one on the FRIEDMAN, and one on the KOCH ranks. In these rank tests, only the resulting values for the interaction are relevant.
	"""
	
	cran = "npIntFactRep" 

	version("1.5", md5="3f49ca7ee0503efc1122a16f11d8ae0a")

	depends_on("r-ez", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
