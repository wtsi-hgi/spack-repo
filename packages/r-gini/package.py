# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGini(RPackage):
	"""Gini Coefficient

	Providing various equations to calculate Gini coefficients.
    The methods used in this package can be referenced from Brown MC (1994) <doi: 10.1016/0277-9536(94)90189-9>.
	"""
	
	cran = "Gini" 

	version("0.1.0", md5="5fd0df767cca646e6ad407e6e4b77019")

