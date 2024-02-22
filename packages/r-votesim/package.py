# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVotesim(RPackage):
	"""Generate Simulated Data for Voting Rules using Evaluations

	Provide functions to generate random simulated evaluations on candidates by voters for evaluation-based elections. Functions are based on several models for continuous or discrete evaluations.
	"""
	
	homepage = "https://eric.univ-lyon2.fr/arolland/"
	cran = "voteSim" 

	version("0.1.1", md5="897e87486aa17355a3d93b83b250e845")

	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
