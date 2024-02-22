# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLss2(RPackage):
	"""The Accelerated Failure Time Model to Right Censored Data Based
on Least-Squares Principle

	Due to lack of proper inference procedure and software,
        the ordinary linear regression model is seldom used in practice
        for the analysis of right censored data. This paper presents an
        S-Plus/R program that implements a recently developed inference
        procedure (Jin, Lin and Ying, 2006) <doi:10.1093/biomet/93.1.147> 
        for the accelerated failure time model based on the least-squares
        principle.
	"""
	
	cran = "lss2" 

	version("1.1", md5="2e3282477af287b713f701bbf70a8548", url="https://cran.r-project.org/src/contrib/lss2_1.1.tar.gz")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
