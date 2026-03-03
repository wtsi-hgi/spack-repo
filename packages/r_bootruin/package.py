# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootruin(RPackage):
	"""A Bootstrap Test for the Probability of Ruin in the Classical
Risk Process

	We provide a framework for testing the probability of ruin in the classical (compound Poisson) risk process. It also includes some procedures for assessing and comparing the performance between the bootstrap test and the test using asymptotic normality.
	"""
	
	cran = "bootruin" 

	version("1.2-4", md5="a735e6e88b9f400317c90fa0292f9ea3")

