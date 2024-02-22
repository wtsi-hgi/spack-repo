# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnifdag(RPackage):
	"""Uniform Sampling of Directed Acyclic Graphs

	Uniform sampling of Directed Acyclic Graphs (DAG) using exact
 enumeration by relating each DAG to a sequence of outpoints (nodes with no
 incoming edges) and then to a composition of integers as suggested by
 Kuipers, J. and Moffa, G. (2015) <doi:10.1007/s11222-013-9428-y>.
	"""
	
	cran = "unifDAG" 

	version("1.0.4", md5="96ec85426894377b2e2b8fb8a92ea637")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
