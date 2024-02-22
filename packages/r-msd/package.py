# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsd(RPackage):
	"""Method of Successive Dichotomizations

	Implements the method of successive dichotomizations by
    Bradley and Massof (2018) <doi:10.1371/journal.pone.0206106>, 
    which estimates item measures, person measures and ordered rating
    category thresholds given ordinal rating scale data. 
	"""
	
	cran = "msd" 

	version("0.3.1", md5="b2b87700597e496fe5da5aab2b6d29cf")

