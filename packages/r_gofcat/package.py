# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofcat(RPackage):
	"""Goodness-of-Fit Measures for Categorical Response Models

	A post-estimation method for categorical response models (CRM). 
    Inputs from objects of class serp(), clm(), polr(), multinom(), mlogit(), 
    vglm() and glm() are currently supported. Available tests include the 
    Hosmer-Lemeshow tests for the binary, multinomial and ordinal logistic 
    regression; the Lipsitz and the Pulkstenis-Robinson tests for the ordinal 
    models. The proportional odds, adjacent-category, and constrained continuation-ratio 
    models are particularly supported at ordinal level. Tests for the proportional 
    odds assumptions in ordinal models are also possible with the Brant and the 
    Likelihood-Ratio tests. Moreover, several summary measures of predictive strength 
    (Pseudo R-squared), and some useful error metrics, including, the brier 
    score, misclassification rate and logloss are also available for the 
    binary, multinomial and ordinal models. Ugba, E. R. and Gertheiss, J. (2018) 
    <http://www.statmod.org/workshops_archive_proceedings_2018.html>.
	"""
	
	cran = "gofcat" 

	version("0.1.2", md5="de269ad8830935ce6d05a67e939f72ee")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-vgam@1.1.4:", type=("build", "run"))
