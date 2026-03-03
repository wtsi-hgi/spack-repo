# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaShrinkage(RPackage):
	"""Meta-Analyses for Simultaneously Estimating Individual Means

	Implement meta-analyses for simultaneously estimating individual means with shrinkage,
 isotonic regression and pretests. Include our original implementation of the isotonic regression via the pool-adjacent-violators algorithm (PAVA) algorithm.
 For the pretest estimator, the confidence interval for individual means are provided.
 Methodologies were published in 
 Taketomi et al. (2021) <doi:10.3390/axioms10040267>, Taketomi et al. (2022) <doi:10.3390/a15010026>, 
 Taketomi et al. (2023-) (under review).
	"""
	
	cran = "meta.shrinkage" 

	version("0.1.4", md5="144fc84da911834b1d5ce9ded8832435")

