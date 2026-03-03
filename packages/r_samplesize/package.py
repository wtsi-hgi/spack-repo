# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesize(RPackage):
	"""Sample Size Calculation for Various t-Tests and Wilcoxon-Test

	Computes sample size for Student's t-test and for the Wilcoxon-Mann-Whitney test for categorical data. The t-test function allows paired and unpaired (balanced / unbalanced) designs as well as homogeneous and heterogeneous variances. The Wilcoxon function allows for ties.
	"""
	
	homepage = "https://github.com/shearer/samplesize"
	cran = "samplesize" 

	version("0.2-4", md5="677040dd543d2bd107793c5bc21b816c")

