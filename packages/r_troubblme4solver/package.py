# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTroubblme4solver(RPackage):
	"""Troubles Solver for 'lme4'

	The main function of the package aims to update 'lmer()'/'glmer()' models depending on their warnings, so trying to avoid convergence and singularity problems.
	"""
	
	homepage = "https://gitlab.com/iagogv/trouBBlme4SolveR"
	cran = "trouBBlme4SolveR" 

	version("0.1.1", md5="0f3a70434ef45a6f785f01e9433a6aff")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lme4@1.1.28:", type=("build", "run"))
