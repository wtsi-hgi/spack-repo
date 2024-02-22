# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromethee(RPackage):
	"""Preference Ranking Organization METHod for Enrichment of
Evaluations

	Functions which can be used to support the Multicriteria Decision Analysis (MCDA) process 
    involving multiple criteria, by PROMETHEE (Preference Ranking Organization METHod for Enrichment of Evaluations).
	"""
	
	cran = "PROMETHEE" 

	version("1.1", md5="cf25aa9e3a9a7a840feb884869ad17fb")

	depends_on("r-lpsolve", type=("build", "run"))
