# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsy(RPackage):
	"""Various Procedures Used in Psychometrics

	Kappa, ICC, reliability coefficient, parallel analysis, 
     multi-traits multi-methods, spherical representation of a correlation matrix.
	"""
	
	cran = "psy" 

	version("1.2", md5="460052abc485f3f33075ce9c04e479af")

