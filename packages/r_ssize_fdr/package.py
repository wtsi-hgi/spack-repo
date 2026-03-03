# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsizeFdr(RPackage):
	"""Sample Size Calculations for Microarray Experiments

	Functions that calculate appropriate sample sizes for one-sample t-tests, two-sample t-tests, and F-tests for microarray experiments based on desired power while controlling for false discovery rates. For all tests, the standard deviations (variances) among genes can be assumed fixed or random.  This is also true for effect sizes among genes in one-sample and two sample experiments. Functions also output a chart of power versus sample size, a table of power at different sample sizes, and a table of critical test values at different sample sizes.
	"""
	
	cran = "ssize.fdr" 

	version("1.3", md5="eb75bd49e86ed03412340e4ba51fc89b")

