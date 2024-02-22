# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmstcompsens(RPackage):
	"""Comparing Restricted Mean Survival Time as Sensitivity Analysis

	Performs two-sample comparisons using the restricted mean survival time (RMST) when survival curves end at different time points between groups. This package implements a sensitivity approach that allows the threshold  timepoint tau to be specified after the longest survival time in the shorter survival group. Two kinds of between-group contrast estimators (the difference in RMST and the ratio of RMST) are computed: Uno et al(2014)<doi:10.1200/JCO.2014.55.2208>, Uno et al(2022)<https://CRAN.R-project.org/package=survRM2>, Ueno and Morita(2023)<doi:10.1007/s43441-022-00484-z>.
	"""
	
	cran = "rmstcompsens" 

	version("0.1.5", md5="47dceec860af06f1f8397390bcbb55dd")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
