# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsDif(RPackage):
	"""Compute Effect Sizes of the Difference

	Computes various effect sizes of the difference, their variance, and confidence interval. This package treats Cohen's d, Hedges' d, biased/unbiased c (an effect size between a mean and a constant) and e (an effect size between means without assuming the variance equality).
	"""
	
	cran = "es.dif" 

	version("1.0.2", md5="ac169b229e0bced1ac8fe915a9362302")

