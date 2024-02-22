# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpscoring(RPackage):
	"""Relative Placement Algorithm

	Implementation of the relative placement algorithm widely used in the scoring of Lindy Hop and West Coast Swing dance contests.
	"""
	
	cran = "RPscoring" 

	version("0.1.0", md5="f79be13c1a1381aa37a596a76fb6e950")

	depends_on("r@3.5:", type=("build", "run"))
