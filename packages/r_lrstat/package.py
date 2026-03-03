# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrstat(RPackage):
	"""Power and Sample Size Calculation for Non-Proportional Hazards
and Beyond

	Performs power and sample size calculation for non-proportional hazards model using the Fleming-Harrington family of weighted log-rank tests. The sequentially calculated log-rank test score statistics are assumed to have independent increments as characterized in Anastasios A. Tsiatis (1982) <doi:10.1080/01621459.1982.10477898>. The mean and variance of log-rank test score statistics are calculated based on Kaifeng Lu (2021) <doi:10.1002/pst.2069>. The boundary crossing probabilities are calculated using the recursive integration algorithm described in Christopher Jennison and Bruce W. Turnbull (2000, ISBN:0849303168). The package can also be used for continuous, binary, and count data. For continuous data, it can handle missing data through mixed-model for repeated measures (MMRM). In crossover designs, it can estimate direct treatment effects while accounting for carryover effects. For binary data, it can design Simon's 2-stage, modified toxicity probability-2 (mTPI-2), and Bayesian optimal interval (BOIN) trials. For count data, it can design group sequential trials for negative binomial endpoints with censoring. Additionally, it facilitates group sequential equivalence trials for all supported data types. Moreover, it can design adaptive group sequential trials for changes in sample size, error spending function, number and spacing or future looks. Finally, it offers various options for adjusted p-values, including graphical and gatekeeping procedures. 
	"""
	
	cran = "lrstat" 

	version("0.2.4", md5="4f0c195aef91a0e35261c0ebefea1bbb")
	version("0.2.2", md5="57420683a9dcd83c11e243c18bfd7423")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-lpsolve@5.6.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
