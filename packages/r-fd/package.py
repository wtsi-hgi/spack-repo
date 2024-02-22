# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFd(RPackage):
	"""Measuring Functional Diversity (FD) from Multiple Traits, and
Other Tools for Functional Ecology

	Computes different multidimensional FD indices.  Implements a distance-based framework to measure FD that allows any number and type of functional traits, and can also consider species relative abundances.  Also contains other useful tools for functional ecology.
	"""
	
	cran = "FD" 

	version("1.0-12.3", md5="8f1ed234859f08334e3cd5dab8ce58f1")

	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
