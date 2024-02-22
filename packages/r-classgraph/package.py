# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassgraph(RPackage):
	"""Construct Graphs of S4 Class Hierarchies

	Construct directed graphs of S4 class hierarchies and
  visualize them.  In general, these graphs typically are DAGs (directed
  acyclic graphs), often simple trees in practice.
	"""
	
	cran = "classGraph" 

	version("0.7-6", md5="ac7cf67ae88c118747313d450c986d2a")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
