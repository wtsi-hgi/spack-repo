# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustanova(RPackage):
	"""Robust One-Way ANOVA Tests under Heteroscedasticity and
Nonnormality

	Robust tests (RW, RPB and RGF) are provided for testing the equality of several long-tailed symmetric (LTS) means when the variances are unknown and arbitrary. RW, RPB and RGF tests are robust versions of Welch's F test proposed by Welch (1951) <doi:10.2307/2332579>, parametric bootstrap test proposed by Krishnamoorthy et. al (2007) <doi:10.1016/j.csda.2006.09.039>; and generalized F test proposed by Weerahandi (1995) <doi:10.2307/2532947>;, respectively. These tests are based on the modified maximum likelihood (MML) estimators proposed by Tiku(1967, 1968) <doi:10.2307/2333859>, <doi:10.1080/01621459.1968.11009228>. 
	"""
	
	cran = "RobustANOVA" 

	version("0.3.0", md5="647fddd5e29393724c43a5358bc3c4e8")

	depends_on("r-peip", type=("build", "run"))
	depends_on("r-optimbase", type=("build", "run"))
