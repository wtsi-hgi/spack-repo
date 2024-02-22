# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPropCombRr(RPackage):
	"""Analyzing Combination of Proportions and Relative Risk

	Carrying out inferences about any linear combination of proportions and the ratio of two proportions.
	"""
	
	cran = "prop.comb.RR" 

	version("1.2", md5="c474abeae63943e7875167b8b5cb635f")

	depends_on("r-rootsolve", type=("build", "run"))
