# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptistock(RPackage):
	"""Determine Optimum Stocking Times Used in Fishery Enhancements

	A collection of functions that aid in calculating the optimum
  time to stock hatchery reared fish into a body of water given the growth, 
  mortality and cost of raising a particular number of individuals to a certain 
  length.
	"""
	
	cran = "optistock" 

	version("0.0.2", md5="a779d538f15ef65fb677055914da5734")

	depends_on("r@2.10:", type=("build", "run"))
