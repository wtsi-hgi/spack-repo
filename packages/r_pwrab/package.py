# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwrab(RPackage):
	"""Power Analysis for AB Testing

	Power analysis for AB testing. The calculations are based on the Welch's unequal variances t-test,
  which is generally preferred over the Student's t-test when sample sizes and variances of the two groups are
  unequal, which is frequently the case in AB testing. In such situations, the Student's t-test will give 
  biased results due to using the pooled standard deviation, unlike the Welch's t-test.
	"""
	
	homepage = "http://github.com/williamcha/pwrAB"
	cran = "pwrAB" 

	version("0.1.0", md5="4f1d9b57ca950899570c6ad1d3d340c4")

	depends_on("r@3.3.1:", type=("build", "run"))
