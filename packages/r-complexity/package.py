# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComplexity(RPackage):
	"""Calculate the Proportion of Permutations in Line with an
Informative Hypothesis

	Allows for the easy computation of complexity: the proportion of the parameter space in line with the hypothesis by chance. The package comes with a Shiny application in which the calculations can be conducted as well. 
	"""
	
	cran = "complexity" 

	version("1.1.2", md5="e9c479845603793e6f9c119ad65dabd1")

	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
