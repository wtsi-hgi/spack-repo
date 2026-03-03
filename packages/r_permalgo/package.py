# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermalgo(RPackage):
	"""Permutational Algorithm to Simulate Survival Data

	This version of the permutational algorithm generates a
        dataset in which event and censoring times are conditional on
        an user-specified list of covariates, some or all of which are
        time-dependent.
	"""
	
	cran = "PermAlgo" 

	version("1.2", md5="f9a2b7993d217ecbeb71f276785ad694")

