# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeukemiaseset(RPackage):
	"""Leukemia's microarray gene expression data (expressionSet).

	Expressionset containing gene expresion data from 60 bone marrow samples of patients with one of the four main types of leukemia (ALL, AML, CLL, CML) or non-leukemia.
	"""
	
	bioc = "leukemiasEset"

	version("1.44.0", commit="15ff27bc27278e2861503c74e4343ce9a2f48c92")
	version("1.38.0", commit="a520d9fe24845854d74ecc4c2114bf5be263e394")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

