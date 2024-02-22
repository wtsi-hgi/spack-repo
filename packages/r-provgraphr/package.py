# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvgraphr(RPackage):
	"""Creates Adjacency Matrices for Lineage Searches

	Creates and manages a provenance graph corresponding to the 
    provenance created by the 'rdtLite' package, which
    collects provenance from R scripts.  'rdtLite' is available on CRAN.
    The provenance format is an extension of the 
    W3C PROV JSON format (<https://www.w3.org/Submission/2013/SUBM-prov-json-20130424/>).
    The extended JSON provenance format is described 
    in <https://github.com/End-to-end-provenance/ExtendedProvJson>.
	"""
	
	cran = "provGraphR" 

	version("1.0.1", md5="30edec6eb55d88f3ed56063fab7e9e49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-provparser@0.2:", type=("build", "run"))
