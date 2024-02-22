# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmsimpute(RPackage):
	"""Generalized Mass Spectrum Missing Peaks Abundance Imputation

	Two-Step Lasso (TS-Lasso) and compound minimum methods to recover 
             the abundance of missing peaks in mass spectrum analysis. TS-Lasso is an 
             imputation method that handles various types of missing peaks simultaneously. This package 
             provides the procedure to generate missing peaks (or data) for simulation study, 
             as well as a tool to estimate and visualize the proportion of missing at random.
	"""
	
	cran = "GMSimpute" 

	version("0.0.1.0", md5="f412b760f5be08305ba0a0dfd57662f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
