# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSquant(RPackage):
	"""Subgroup Identification Based on Quantitative Objectives

	A subgroup identification method for precision medicine based on 
    quantitative objectives. This method can handle continuous, binary and 
    survival endpoint for both prognostic and predictive case. For the 
    predictive case, the method aims at identifying a subgroup for which 
    treatment is better than control by at least a pre-specified or 
    auto-selected constant. For the prognostic case, the method aims at 
    identifying a subgroup that is at least better than a 
    pre-specified/auto-selected constant. The derived signature is a linear 
    combination of predictors, and the selected subgroup are subjects with 
    the signature > 0. The false discover rate when no true subgroup exists
    is strictly controlled at a user-specified level.
	"""
	
	cran = "squant" 

	version("1.1.4", md5="3d4be8ce311b4470bcaca9b81b370cdb")

	depends_on("r-glmnet@2.0.13:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
