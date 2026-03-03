# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollapselevels(RPackage):
	"""Collapses Levels, Computes Information Value and WoE

	Contains functions to help in selecting and exploring features ( or variables ) in binary classification problems.
             Provides functions to compute and display information value and weight of evidence (WoE) of the variables , and to convert numeric variables to categorical variables by binning.
             Functions are also provided  to determine which levels ( or categories ) of a categorical variable can be collapsed (or combined ) based on their response rates.
             The functions provided only work for binary classification problems.
	"""
	
	cran = "CollapseLevels" 

	version("0.3.0", md5="9501808c4315cc92af847c2b17b0249e")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
