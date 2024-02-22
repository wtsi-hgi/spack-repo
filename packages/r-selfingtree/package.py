# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelfingtree(RPackage):
	"""Genotype Probabilities in Intermediate Generations of Inbreeding
Through Selfing

	A probability tree allows to compute probabilities of
	     complex events, such as genotype probabilities in intermediate generations of inbreeding
	     through recurrent self-fertilization (selfing). This package implements functionality to compute
	     probability trees for two- and three-marker genotypes in the F2 to F7 selfing
	     generations. The conditional probabilities are derived automatically
	     and in symbolic form. The package also provides functionality to
	     extract and evaluate the relevant probabilities.
	"""
	
	cran = "selfingTree" 

	version("0.2", md5="193d06a7fdf57aaa9ce5dd24c5343b0d")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
