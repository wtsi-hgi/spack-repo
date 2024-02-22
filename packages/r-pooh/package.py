# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPooh(RPackage):
	"""Partial Orders and Relations

	Finds equivalence classes corresponding to a symmetric relation
    or undirected graph.  Finds total order consistent with partial order
    or directed graph (so-called topological sort).
	"""
	
	homepage = "http://www.stat.umn.edu/geyer/pooh/"
	cran = "pooh" 

	version("0.3-2", md5="f660d86931fdb329c22195dab809d2ff")

	depends_on("r@3.0.2:", type=("build", "run"))
