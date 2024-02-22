# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnesrake(RPackage):
	"""ANES Raking Implementation

	Provides a comprehensive system for selecting
    variables and weighting data to match the specifications of the American
    National Election Studies. The package includes methods for identifying
    discrepant variables, raking data, and assessing the effects of the raking
    algorithm. It also allows automated re-raking if target variables fall
    outside identified bounds and allows greater user specification than other
    available raking algorithms. A variety of simple weighted statistics that
    were previously in this package (version .55 and earlier) have been moved to
    the package 'weights.'
	"""
	
	cran = "anesrake" 

	version("0.80", md5="28c5893f511eb44e0850df7f936532eb")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
