# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPocrm(RPackage):
	"""Dose Finding in Drug Combination Phase I Trials Using PO-CRM

	Provides functions to implement and simulate the partial order continual reassessment method (PO-CRM) of Wages, Conaway and O'Quigley (2011) <doi:10.1177/1740774511408748> for use in Phase I trials of combinations of agents. Provides a function for generating a set of initial guesses (skeleton) for the toxicity probabilities at each combination that correspond to the set of possible orderings of the toxicity probabilities specified by the user.
	"""
	
	cran = "pocrm" 

	version("0.13", md5="a075b6c2a6f2a77c72caee519a14a1df")

	depends_on("r-dfcrm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
