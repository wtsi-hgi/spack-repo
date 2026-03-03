# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychometric(RPackage):
	"""Applied Psychometric Theory

	Contains functions useful for correlation theory, 
    meta-analysis (validity-generalization), reliability, 
    item analysis, inter-rater reliability, and classical utility.
	"""
	
	cran = "psychometric" 

	version("2.4", md5="b70dfd43542631b9a7e0d49e074344db")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-multilevel", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
