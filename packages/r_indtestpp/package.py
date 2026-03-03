# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndtestpp(RPackage):
	"""Tests of Independence and Analysis of Dependence Between Point
Processes in Time

	It provides a general framework to analyse dependence between point processes in time. It includes parametric and non-parametric tests to study independence,  and functions for generating and analysing  different types of dependence.
	"""
	
	cran = "IndTestPP" 

	version("3.0", md5="f7a54d4f46baaf7b362685529aa00301")

	depends_on("r@2.10:", type=("build", "run"))
