# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscp(RPackage):
	"""Multiscale Change Point Detection via Gradual Bandwidth
Adjustment in Moving Sum Processes

	Multiscale moving sum procedure for the detection of changes in expectation in univariate sequences. References - Multiscale change point detection via gradual bandwidth adjustment in moving sum processes (2021+), Tijana Levajkovic and Michael Messer.
	"""
	
	cran = "mscp" 

	version("1.0", md5="c9d1fee706e1c7a8b702a19893fb6634")

