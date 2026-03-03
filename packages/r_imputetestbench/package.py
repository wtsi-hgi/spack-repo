# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputetestbench(RPackage):
	"""Test Bench for the Comparison of Imputation Methods

	Provides a test bench for the comparison of missing data imputation 
    methods in uni-variate time series. Imputation methods are compared using 
    different error metrics. Proposed imputation methods and alternative error 
    metrics can be used.
	"""
	
	cran = "imputeTestbench" 

	version("3.0.3", md5="a5122f33abcc89d870cc6b2da9469e3c")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
