# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListest(RPackage):
	"""Tests of independence based on the Longest Increasing
Subsequence

	Tests for independence between X and Y computed from a paired sample (x1,y1),...(xn,yn) of (X,Y), using one of the following statistics (a) the Longest Increasing Subsequence (Ln), (b) JLn, a Jackknife version of Ln or (c) JLMn, a Jackknife version of the longest monotonic subsequence. This family of tests can be applied under the assumption of continuity of X and Y.
	"""
	
	cran = "LIStest" 

	version("2.1", md5="4942081da14384246beff8e3970c4b43")

	depends_on("r@2.10:", type=("build", "run"))
