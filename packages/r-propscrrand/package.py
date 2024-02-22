# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPropscrrand(RPackage):
	"""Propensity Score Methods for Assigning Treatment in Randomized
Trials

	Contains functions to run propensity-biased allocation to balance covariate distributions in sequential trials and propensity-constrained randomization to balance covariate distributions in trials with known baseline covariates at time of randomization.  Currently only supports trials comparing two groups.
	"""
	
	cran = "PropScrRand" 

	version("1.1.1", md5="1956e836b1b2215ecb0ef20b91be4bf2")

