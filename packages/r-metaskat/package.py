# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaskat(RPackage):
	"""Meta Analysis for SNP-Set (Sequence) Kernel Association Test

	Functions for Meta-analysis Burden Test, Sequence Kernel Association Test (SKAT) and Optimal SKAT (SKAT-O) by  Lee et al. (2013) <doi:10.1016/j.ajhg.2013.05.010>. These methods use summary-level score statistics to carry out gene-based meta-analysis for rare variants.
	"""
	
	cran = "MetaSKAT" 

	version("0.82", md5="d60d689dfeb8b45d56f5bcfc66659c6b")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-skat@2.0.1:", type=("build", "run"))
