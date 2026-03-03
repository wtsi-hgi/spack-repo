# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsgsis(RPackage):
	"""Two Stage-Grouped Sure Independence Screening

	To provide a high dimensional grouped variable selection approach for detection of whole-genome SNP effects and SNP-SNP interactions, as described in Fang et al. (2017, under review).
	"""
	
	cran = "TSGSIS" 

	version("0.1", md5="bef892538ea8206953f6a6ba24da8b70")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
