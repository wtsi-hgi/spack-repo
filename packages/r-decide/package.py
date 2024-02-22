# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecide(RPackage):
	"""DEComposition of Indirect and Direct Effects

	Calculates various estimates for measures of educational
        differentials, the relative importance of primary and secondary
        effects in the creation of such differentials and compares the
        estimates obtained from two datasets.
	"""
	
	cran = "DECIDE" 

	version("1.3", md5="70b655b13eb7ca5e2a83aa35f74fab6c")

