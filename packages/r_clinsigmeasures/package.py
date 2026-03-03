# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinsigmeasures(RPackage):
	"""Clinical Significance Measures

	Provides measures of effect sizes from summarized continuous variables as well as diagnostic accuracy statistics for 2x2 table data. Includes functions for Cohen's d, Cohen's q, partial eta-squared, coefficient of variation, odds ratio, likelihood ratios, sensitivity, specificity, positive and negative predictive values, and Youden index.
	"""
	
	cran = "ClinSigMeasures" 

	version("1.0", md5="21194e724b69b32f02ec2538efd08aed")

