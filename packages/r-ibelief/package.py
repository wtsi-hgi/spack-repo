# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbelief(RPackage):
	"""Belief Function Implementation

	Some basic functions to implement belief functions including:
    transformation between belief functions using the method introduced by
    Philippe Smets <arXiv:1304.1122>, evidence combination, evidence
    discounting, decision-making, and constructing masses. Currently, thirteen
    combination rules and six decision rules are supported. It can also be
    used to generate different types of random masses when working on belief
    combination and conflict management.
	"""
	
	cran = "ibelief" 

	version("1.3.1", md5="be2b4ce58de3ecc0aed80170ce0749dc")

	depends_on("r@3.2.1:", type=("build", "run"))
