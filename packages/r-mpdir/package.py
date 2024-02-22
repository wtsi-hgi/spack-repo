# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpdir(RPackage):
	"""Data Sets and Scripts for Modeling Psychophysical Data in R

	Data sets and scripts for Modeling Psychophysical Data in R (Springer).
	"""
	
	cran = "MPDiR" 

	version("0.2", md5="5797fa47ace568f0539aa9e074d38321")

	depends_on("r@3.5:", type=("build", "run"))
