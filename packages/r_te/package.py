# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTe(RPackage):
	"""Insertion/Deletion Dynamics for Transposable Elements

	Provides functions to estimate the insertion and deletion rates of transposable element (TE) families. The estimation of insertion rate consists of an improved estimate of the age distribution that takes into account random mutations, and an adjustment by the deletion rate. A hypothesis test for a uniform insertion rate is also implemented. This package implements the methods proposed in Dai et al (2018).
	"""
	
	cran = "TE" 

	version("0.3-0", md5="2eaaad21ac609c787d1e442da5a05bc6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rainbow", type=("build", "run"))
