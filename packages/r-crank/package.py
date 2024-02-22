# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrank(RPackage):
	"""Completing Ranks

	Functions for completing and recalculating rankings and sorting.
	"""
	
	cran = "crank" 

	version("1.1-2", md5="f0c8635c47dcae52ee249cdac17dfce8")

