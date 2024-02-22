# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparec(RPackage):
	"""Compare Two Correlated C Indices with Right-Censored Survival
Outcome

	Proposed by Harrell, the C index or concordance C, is considered an overall measure of discrimination in survival analysis between a survival outcome that is possibly right censored and a predictive-score variable, which can represent a measured biomarker or a composite-score output from an algorithm that combines multiple biomarkers. This package aims to statistically compare two C indices with right-censored survival outcome, which commonly arise from a paired design and thus resulting two correlated C indices.
	"""
	
	cran = "compareC" 

	version("1.3.2", md5="f789213cee4c511160f2776cedd29be6")

