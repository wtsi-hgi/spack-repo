# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubformula(RPackage):
	"""Create Subformulas of a Formula

	A formula 'sub' is a subformula of 'formula' if all the terms
    on the right hand side of 'sub' are terms of 'formula' and their left hand 
    sides are identical. This package aids in the creation of subformulas.
	"""
	
	homepage = "https://github.com/JonasMoss/subformula"
	cran = "subformula" 

	version("0.1.0", md5="6fe419161107a2f4e109d0e183fa4ac6")

