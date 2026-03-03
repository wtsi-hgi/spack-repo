# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesize4clinicaltrials(RPackage):
	"""Sample Size Calculation for the Comparison of Means or
Proportions in Phase III Clinical Trials

	There are four categories of Phase III clinical trials according to different research goals, including (1) Testing for equality, (2) Superiority trial, (3) Non-inferiority trial, and (4) Equivalence trial. This package aims to help researchers to calculate sample size when comparing means or proportions in Phase III clinical trials with different research goals.
	"""
	
	cran = "SampleSize4ClinicalTrials" 

	version("0.2.3", md5="2991d78e45b4b38c199729c545b5d130")

