# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistinctiveness(RPackage):
	"""Distinctiveness Centrality

	Calculates Distinctiveness Centrality in social networks. 
	For formulas and descriptions, see Fronzetti Colladon and Naldi (2020) <doi:10.1371/journal.pone.0233276>.
	"""
	
	homepage = "https://github.com/iandreafc/distinctiveness-R"
	cran = "distinctiveness" 

	version("1.0.1", md5="d19d3c57d423d0825e1739b0e3821ff1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
