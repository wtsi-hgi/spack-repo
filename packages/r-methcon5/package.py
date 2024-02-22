# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethcon5(RPackage):
	"""Identify and Rank CpG DNA Methylation Conservation Along the
Human Genome

	Identify and rank CpG DNA methylation conservation along the human 
    genome. Specifically it includes bootstrapping methods to provide ranking 
    which should adjust for the differences in length as without it short 
    regions tend to get higher conservation scores.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/methcon5"
	cran = "methcon5" 

	version("0.1.0", md5="12dea31fd8c4fe3400a0e152d91f4d47", url="https://cran.r-project.org/src/contrib/methcon5_0.1.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
