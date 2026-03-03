# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirtsvd(RPackage):
	"""SVD-Based Estimation for Exploratory Item Factor Analysis

	Provides singular value decomposition based estimation algorithms for exploratory item factor analysis (IFA) 
    based on multidimensional item response theory models. For more information, please refer to:
    Zhang, H., Chen, Y., & Li, X. (2020). A note on exploratory item factor analysis by 
    singular value decomposition. Psychometrika, 1-15, <DOI:10.1007/s11336-020-09704-7>.
	"""
	
	cran = "mirtsvd" 

	version("1.0", md5="54df9720378302e4089c0ac810b6ab34")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-mirtjml", type=("build", "run"))
