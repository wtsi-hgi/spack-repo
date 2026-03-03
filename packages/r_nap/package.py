# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNap(RPackage):
	"""Non-Local Alternative Priors in Psychology

	Conducts Bayesian Hypothesis tests of a point null hypothesis against a two-sided alternative
             using Non-local Alternative Prior (NAP) for one- and two-sample z- and t-tests 
             (Pramanik and Johnson, 2022). Under the alternative, the NAP is assumed on the standardized 
             effects size in one-sample tests and on their differences in two-sample tests. The package 
             considers two types of NAP densities: (1) the normal moment prior, and (2) the composite alternative. 
             In fixed design tests, the functions calculate the Bayes factors and the expected weight of evidence
             for varied effect size and sample size. The package also provides a sequential testing framework using the
             Sequential Bayes Factor (SBF) design. The functions calculate the operating characteristics (OC)
             and the average sample number (ASN), and also conducts sequential tests for a sequentially observed data.
	"""
	
	cran = "NAP" 

	version("1.1", md5="6891d29ef1acf74488232fcca9178ec4")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
