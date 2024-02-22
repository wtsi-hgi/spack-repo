# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeat(RPackage):
	"""Efficient Network Enrichment Analysis Test

	Includes functions and examples to compute NEAT, the Network
    Enrichment Analysis Test described in Signorelli et al.  (2016,
    <DOI:10.1186/s12859-016-1203-6>).
	"""
	
	homepage = "https://mirkosignorelli.github.io/r"
	cran = "neat" 

	version("1.2.4", md5="0d8887c759b42ca83262b3f40dd55345")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
