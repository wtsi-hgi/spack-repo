# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdtoolkit(RPackage):
	"""Collection of Tools for PD Rating Model Development and
Validation

	The goal of this package is to cover the most common steps in probability of default (PD) rating model development and validation. 
	     The main procedures available are those that refer to univariate, bivariate, multivariate analysis, calibration and validation. 
	     Along with accompanied 'monobin' and 'monobinShiny' packages, 'PDtoolkit' provides functions which are suitable for different 
	     data transformation and modeling tasks such as: 
	     imputations, monotonic binning of numeric risk factors, binning of categorical risk factors, weights of evidence (WoE) and 
	     information value (IV) calculations, WoE coding (replacement of risk factors modalities with WoE values), risk factor clustering, 
	     area under curve (AUC) calculation and others. Additionally, package provides set of validation functions for testing homogeneity, 
	     heterogeneity, discriminatory and predictive power of the model.
	"""
	
	homepage = "https://github.com/andrija-djurovic/PDtoolkit"
	cran = "PDtoolkit" 

	version("1.2.0", md5="fcbadd420984816f309a7b06d193d868")

	depends_on("r-monobin", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
