# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpp(RPackage):
	"""Composition of Probabilistic Preferences (CPP)

	CPP is a multiple criteria decision method to evaluate alternatives on complex decision making problems, by a probabilistic approach. The CPP was created and expanded by Sant'Anna, Annibal P. (2015) <doi:10.1007/978-3-319-11277-0>.
	"""
	
	cran = "CPP" 

	version("0.1.0", md5="6e4e3716f67728410771bc94be4350db")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-kappalab", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
