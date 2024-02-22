# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyndi(RPackage):
	"""Synthetic Data Integration

	Regression inference for multiple populations by integrating 
    summary-level data using stacked imputations. Gu, T., Taylor, J.M.G. and 
    Mukherjee, B. (2021) A synthetic data integration framework to leverage 
    external summary-level information from heterogeneous populations 
    <arXiv:2106.06835>.
	"""
	
	homepage = "https://github.com/umich-biostatistics/SynDI"
	cran = "SynDI" 

	version("0.1.0", md5="1e4457dab24a0b56209bb809f3ded844")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stackimpute", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
