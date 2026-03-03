# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbsdiff(RPackage):
	"""Satorra-Bentler Scaled Chi-Squared Difference Test

	Calculates a Satorra-Bentler scaled chi-squared difference test between nested models that were estimated using maximum likelihood (ML) with robust standard errors, which cannot be calculated the traditional way. For details see Satorra & Bentler (2001) <doi:10.1007/bf02296192> and Satorra & Bentler (2010) <doi:10.1007/s11336-009-9135-y>. This package may be particularly helpful when used in conjunction with 'Mplus' software, specifically when implementing the complex survey option. In such cases, the model estimator in 'Mplus' defaults to ML with robust standard errors.    
	"""
	
	cran = "SBSDiff" 

	version("0.1.0", md5="2836f555d388b2fd998a5c1c57b8a0c4")

