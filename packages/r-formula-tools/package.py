# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RFormulaTools(RPackage):
	"""Programmatic Utilities for Manipulating Formulas, Expressions,
Calls, Assignments and Other R Objects

	These utilities facilitate the programmatic manipulations of
    formulas, expressions, calls, assignments and other R language objects. 
    These objects all share the same structure: a left-hand side, operator and 
    right-hand side. This packages provides methods for accessing and 
    modifying this structures as well as extracting and replacing names and 
    symbols from these objects.
	"""
	
	homepage = "https://github.com/decisionpatterns/formula.tools"
	cran = "formula.tools" 

	version("1.7.1", md5="ab6ac9a593b99ef94148b2c908abc07d")

	depends_on("r@3.0.0:", type=("build", "run"))
	depends_on("r-operator-tools@1.4.0:", type=("build", "run"))
