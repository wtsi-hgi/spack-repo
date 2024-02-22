# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkewsamp(RPackage):
	"""Estimate Sample Sizes for Group Comparisons with Skewed
Distributions

	Estimate necessary sample sizes for comparing the location
    of data from two groups or categories when the distribution of the 
    data is skewed. The package 
    offers a non-parametric method for a Wilcoxon Mann-Whitney test of 
    location shift as well as methods for several generalized linear 
    models, for instance, Gamma regression.
	"""
	
	cran = "skewsamp" 

	version("1.0.0", md5="dbf1f51068a3c4778c8bcf5a33f51570")

