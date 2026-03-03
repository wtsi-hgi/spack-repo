# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrnaimm(RPackage):
	"""Performing Single-Cell RNA-Seq Imputation by Using Mean/Median
Imputation

	Performing single-cell imputation in a way that preserves the biological variations in the data. The package clusters the input data to do imputation for each cluster, and do a distribution check using the Anderson-Darling normality test to impute dropouts using mean or median (Yazici, B., & Yolacan, S. (2007) <DOI:10.1080/10629360600678310>).
	"""
	
	cran = "ScRNAIMM" 

	version("0.1", md5="b65eb20a1061544524b576c23ae343fe")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-scdha", type=("build", "run"))
