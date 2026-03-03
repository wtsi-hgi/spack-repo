# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpowersamplesize(RPackage):
	"""Sample Size Computations Controlling the Type-II Generalized
Family-Wise Error Rate

	The significance of mean difference tests in clinical trials is established if at least r null hypotheses are rejected among m that are simultaneously tested. This package enables one to compute necessary sample sizes for single-step (Bonferroni) and step-wise procedures (Holm and Hochberg). These three procedures control the q-generalized family-wise error rate (probability of making at least q false rejections). Sample size is computed (for these single-step and step-wise procedures) in a such a way that the r-power (probability of rejecting at least r false null hypotheses, i.e. at least r significant endpoints among m) is above some given threshold, in the context of tests of difference of means for two groups of continuous endpoints (variables). Various types of structure of correlation are considered. It is also possible to analyse data (i.e., actually test difference in means) when these are available. The case r equals 1 is treated in separate functions that were used in Lafaye de Micheaux et al. (2014) <doi:10.1080/10543406.2013.860156>.
	"""
	
	cran = "rPowerSampleSize" 

	version("1.0.2", md5="91f854d4c581ea7e5c7488feeea9f3dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ssanv", type=("build", "run"))
