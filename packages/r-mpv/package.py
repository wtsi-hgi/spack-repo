# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpv(RPackage):
	"""Data Sets from Montgomery, Peck and Vining

	Most of this package consists of data sets from the 
             textbook Introduction
             to Linear Regression Analysis, by Montgomery, Peck
             and Vining.  All data sets from the 3rd edition are included
             and many from the 6th edition are also included.
             The package also contains some additional data sets and functions.
	"""
	
	cran = "MPV" 

	version("1.63", md5="75d80f99d67ececb16af02d88704f4a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
