# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatpsych(RPackage):
	"""Statistical Methods for Psychologists

	Implements confidence interval and sample size methods that are especially useful in psychological research. The methods can be applied in 1-group, 2-group, paired-samples, and multiple-group designs and to a variety of parameters including means, medians, proportions, slopes, standardized mean differences, standardized linear contrasts of means, plus several measures of correlation and association. The confidence intervals and sample size functions are applicable to single parameters as well as differences, ratios, and linear contrasts of parameters.  The sample size functions can be used to approximate the sample size needed to estimate a parameter or function of parameters with desired confidence interval precision or to perform a variety of hypothesis tests (directional two-sided, equivalence, superiority, noninferiority) with desired power. For details see:  Statistical Methods for Psychologists, Volumes 1 – 4, <https://dgbonett.sites.ucsc.edu/>.     
	"""
	
	cran = "statpsych" 

	version("1.5.0", md5="5a0509f43da945cd1fffd94fd4c7bfec")

	depends_on("r-mnonr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
