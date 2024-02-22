# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmstable(RPackage):
	"""Finite Moment Stable Distributions

	Some basic procedures for dealing
        with log maximally skew stable distributions, which are also
        called finite moment log stable distributions.
	"""
	
	cran = "FMStable" 

	version("0.1-4", md5="3697fa5f8c5cc6acfcf0285ca7819f56")

