# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobstattm(RPackage):
	"""Robust Statistics: Theory and Methods

	Companion package for the book: "Robust Statistics: Theory and Methods, second edition", <http://www.wiley.com/go/maronna/robust>.  This package contains code that implements the robust estimators discussed in the recent second edition of the book above, as well as the scripts reproducing all the examples in the book.
	"""
	
	cran = "RobStatTM" 

	version("1.0.8", md5="a0a14444a46e0b1b8367e1249b3af530")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pyinit", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
