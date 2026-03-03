# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIscocrosswalks(RPackage):
	"""Crosswalks Between Classifications of Occupations

	Allows the user to perform approximate
 matching between the occupational classifications using concordances provided by
 the Institute for Structural Research and Faculty of Economics, University of
 Warsaw, <doi:10.1111/ecot.12145>. The crosswalks offer a complete
 step-by-step mapping of Standard Occupational Classification (2010) data to the
 International Standard Classification of Occupations (2008). We propose a
 mapping method based on the aforementioned research that converts measurements
 to the smallest possible unit of the target taxonomy, and then performs an
 aggregation/estimate to the requested degree Occupational Hierarchical level.
	"""
	
	homepage = "https://github.com/eworx-org/iscoCrosswalks"
	cran = "iscoCrosswalks" 

	version("1.0.0", md5="d6efabc215848dc3eadd105b4d1b1558")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-labourr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
