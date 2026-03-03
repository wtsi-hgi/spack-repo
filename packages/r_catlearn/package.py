# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatlearn(RPackage):
	"""Formal Psychological Models of Categorization and Learning

	Formal psychological models of categorization and learning, independently-replicated data sets against which to test them, and simulation archives.
	"""
	
	cran = "catlearn" 

	version("1.0", md5="1eaab3875e43c91eb0db177de3ec8c52")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.7.5:", type=("build", "run"))
