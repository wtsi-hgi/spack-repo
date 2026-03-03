# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhppp(RPackage):
	"""Simulating Nonhomogeneous Poisson Point Processes

	Simulates events from one dimensional nonhomogeneous Poisson point processes (NHPPPs). Functions are based on three algorithms that provably sample from a target NHPPP: the time-transformation of a homogeneous Poisson process (of intensity one) via the inverse of the integrated intensity function (Cinlar E, "Theory of stochastic processes" (1975, ISBN:0486497996)); the generation of a Poisson number of order statistics from a fixed density function; and the thinning of a majorizing NHPPP via an acceptance-rejection scheme (Lewis PAW, Shedler, GS (1979) <doi:10.1002/nav.3800260304>).
	"""
	
	homepage = "https://github.com/bladder-ca/nhppp-fast"
	cran = "nhppp" 

	version("0.1.3", md5="4f0a4a1d92660f375a134742289fe529")

	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rstream", type=("build", "run"))
