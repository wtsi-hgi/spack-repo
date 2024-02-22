# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtvc(RPackage):
	"""Multiple Counting Process Structure for Survival Analysis

	Counting process structure is fundamental to model time varying covariates.
    This package restructures dataframes in the counting process format for one or more variables.
    F. W. Dekker, et al. (2008) <doi:10.1038/ki.2008.328>.
	"""
	
	homepage = "https://github.com/egonzato/mtvc"
	cran = "mtvc" 

	version("1.1.0", md5="bf9ca88e25b455b58d32f55d9fa6f0d9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
