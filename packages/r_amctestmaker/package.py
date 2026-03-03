# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmctestmaker(RPackage):
	"""Generate LaTeX Code for Auto-Multiple-Choice (AMC)

	Generate code for use with the Optical Mark Recognition free software Auto Multiple Choice (AMC). More specifically, this package provides functions that use as input the question and answer texts, and output the LaTeX code for AMC.
	"""
	
	cran = "AMCTestmakeR" 

	version("1.0.0", md5="5b938b1ef227592434eae7eedb45e9f3")

