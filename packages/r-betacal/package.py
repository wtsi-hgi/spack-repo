# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetacal(RPackage):
	"""Beta Calibration

	Fit beta calibration models and obtain calibrated probabilities from
    them.
	"""
	
	cran = "betacal" 

	version("0.1.0", md5="f3afb8308b56d70641d6d6a4621a95c6")

