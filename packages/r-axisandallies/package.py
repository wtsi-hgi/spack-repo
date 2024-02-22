# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAxisandallies(RPackage):
	"""Axis and Allies Spring

	Simulates battles in the board game Axis and Allies Spring 1942, and calculates your probability of winning a battle. This speeds the game up significantly.
	"""
	
	cran = "axisandallies" 

	version("0.1.0", md5="4d309a8e36d0ef4fb3d8c7725f2b0bac")

