# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTnlTest(RPackage):
	"""Non-Parametric Tests for the Two-Sample Problem

	Performing the hypothesis tests for the two
    sample problem based on order statistics and power comparisons. 
    Calculate the test statistic, density, distribution function, 
    quantile function, random number generation and others.
	"""
	
	homepage = "https://github.com/ihababusaif/tnl.Test"
	cran = "tnl.Test" 

	version("0.1.0", md5="b474cd14ee7bf7af9b10b2511bd22741")

	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
