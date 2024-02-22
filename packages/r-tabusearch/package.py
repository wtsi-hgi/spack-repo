# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabusearch(RPackage):
	"""Tabu Search Algorithm for Binary Configurations

	Tabu search algorithm for binary configurations. A basic version of the algorithm as described by Fouskakis and Draper (2007) <doi:10.1111/j.1751-5823.2002.tb00174.x>.
	"""
	
	cran = "tabuSearch" 

	version("1.1.1", md5="a581afdc609d9e4e6f5f8e1b02381fbe")

