# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class ROperatorTools(RPackage):
	"""Utilities for Working with R's Operators

	Provides a collection of utilities that allow programming with 
    R's operators. Routines allow classifying operators, 
    translating to and from an operator and its underlying function, and inverting 
    some operators (e.g. comparison operators), etc. All methods can be extended
    to custom infix operators. 
	"""
	
	homepage = "https://github.com/decisionpatterns/operator.tools"
	cran = "operator.tools" 

	version("1.6.3", md5="16c236522901759bd83488e736e406aa")
