# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhrases(RPackage):
	"""Phrasal Verbs in English Club Website

	Contains all phrasal verbs listed in <https://www.englishclub.com/ref/Phrasal_Verbs/>
            as data frame. Useful for educational purpose as well as for text mining.
	"""
	
	homepage = "https://github.com/sumanstats/phrases"
	cran = "phrases" 

	version("0.1", md5="abadd13c2be18461e16b5403be732384")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
