# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalhypergraph(RPackage):
	"""Drawing Causal Hypergraphs

	Draws causal hypergraph plots from models output by configurational comparative methods such as Coincidence Analysis (CNA) or Qualitative Comparative Analysis (QCA).
	"""
	
	cran = "causalHyperGraph" 

	version("0.1.0", md5="5df4215ff245685ba908dd5988b3c963")

	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-diagrammersvg", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-useful", type=("build", "run"))
	depends_on("r-cna", type=("build", "run"))
