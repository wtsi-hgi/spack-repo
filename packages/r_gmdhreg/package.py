# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmdhreg(RPackage):
	"""Regression using GMDH Algorithms

	Regression using GMDH algorithms from Prof. Alexey G. Ivakhnenko.
    Group Method of Data Handling (GMDH), or polynomial neural networks, is a family of inductive algorithms
    that performs gradually complicated polynomial models and selecting the best solution by an external criterion.
    In other words, inductive GMDH algorithms give possibility finding automatically interrelations in data, and
    selecting an optimal structure of model or network.
    The package includes GMDH Combinatorial, GMDH MIA (Multilayered Iterative Algorithm), GMDH GIA (Generalized Iterative Algorithm) and GMDH Combinatorial with Active Neurons.
	"""
	
	cran = "GMDHreg" 

	version("0.2.3", md5="ff239255aec68f312ca1cdfa0c0b5708")

	depends_on("r@2.15:", type=("build", "run"))
