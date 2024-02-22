# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFso(RPackage):
	"""Fuzzy Set Ordination

	Fuzzy set ordination is a multivariate analysis used in ecology to
    relate the composition of samples to possible explanatory variables.  While
    differing in theory and method, in practice, the use is similar to 'constrained
    ordination.'  The package contains plotting and summary functions as well as
    the analyses.  
	"""
	
	cran = "fso" 

	version("2.1-2", md5="1e8f2e43b6d9716bb98f8a685768fe40")

	depends_on("r-labdsv", type=("build", "run"))
