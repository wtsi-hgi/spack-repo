# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStackimpute(RPackage):
	"""Tools for Analysis of Stacked Multiple Imputations

	Provides methods for inference using stacked multiple 
    imputations augmented with weights. The vignette provides example R code for 
    implementation in general multiple imputation settings. For additional details 
    about the estimation algorithm, we refer the reader to Beesley, Lauren J and 
    Taylor, Jeremy M G (2020) “A stacked approach for chained equations multiple 
    imputation incorporating the substantive model” <doi:10.1111/biom.13372>, 
    and Beesley, Lauren J and Taylor, Jeremy M G (2021) “Accounting for not-at-random 
    missingness through imputation stacking” <arXiv:2101.07954>.
	"""
	
	cran = "StackImpute" 

	version("0.1.0", md5="75cdc0aeba4c138f95a036dc0413ac1a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
