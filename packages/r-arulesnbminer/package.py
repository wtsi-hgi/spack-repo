# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArulesnbminer(RPackage):
	"""Mining NB-Frequent Itemsets and NB-Precise Rules

	NBMiner is an implementation of the model-based mining algorithm for mining NB-frequent itemsets and NB-precise rules. Michael Hahsler (2006) <doi:10.1007/s10618-005-0026-2>. 
	"""
	
	homepage = "https://github.com/mhahsler/arulesNBMiner"
	cran = "arulesNBMiner" 

	version("0.1-8", md5="2095bf88ec64c5cec9e2bb708487469d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-arules@1.6.0:", type=("build", "run"))
	depends_on("r-rjava@0.9.0:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
