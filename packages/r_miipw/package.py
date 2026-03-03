# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiipw(RPackage):
	"""IPW and Mean Score Methods for Time-Course Missing Data

	Contains functions for data analysis of Repeated measurement using GEE. Data may contain missing value in response and covariates. For parameter estimation through Fisher Scoring algorithm, Mean Score and Inverse Probability Weighted method combining with Multiple Imputation are used when there is missing value in covariates/response.
             Reference for mean score method, inverse probability weighted method is
             Wang et al(2007)<doi:10.1093/biostatistics/kxl024>.
	"""
	
	cran = "MIIPW" 

	version("0.1.1", md5="a1b0ed07177e76d2b65d525bd12dafc5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
