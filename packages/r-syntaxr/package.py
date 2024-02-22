# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyntaxr(RPackage):
	"""An 'SPSS' Syntax Generator for Multi-Variable Manipulation

	A set of functions for generating 'SPSS' syntax files from the R environment.
	"""
	
	homepage = "https://github.com/greenmeen/syntaxr"
	cran = "syntaxr" 

	version("0.8.0", md5="5143f3ddb0cc892d4de68c2567f83313")

	depends_on("r-magrittr", type=("build", "run"))
