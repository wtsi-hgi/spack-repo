# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighestmedianrules(RPackage):
	"""Implementation of Voting Rules Electing the Candidate with
Highest Median Grade

	Computes the scores and ranks candidates according to voting rules electing the highest median grade.
    Based on "Tie-breaking the highest median: alternatives to the majority judgment", A. Fabre, Social Choice & Welfare (forthcoming as of 2020). The paper is available here: <https://github.com/bixiou/highest_median/raw/master/Tie-breaking%20Highest%20Median%20-%20Fabre%202019.pdf>.
    Functions to plot the voting profiles can be found on github: <https://github.com/bixiou/highest_median/blob/master/packages_functions_data.R>.
	"""
	
	cran = "HighestMedianRules" 

	version("1.0", md5="0cf72c15d07a5818a2917259e3ff268b")

	depends_on("r-rmallow", type=("build", "run"))
