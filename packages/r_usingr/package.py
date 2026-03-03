# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsingr(RPackage):
	"""Data Sets, Etc. for the Text "Using R for Introductory
Statistics", Second Edition

	A collection of data sets to accompany the
    textbook "Using R for Introductory Statistics," second
    edition.
	"""
	
	cran = "UsingR" 

	version("2.0-7", md5="6f60d699d48419f8106cf94c7ebf00cb")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-histdata", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
