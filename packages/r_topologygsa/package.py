# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopologygsa(RPackage):
	"""Gene Set Analysis Exploiting Pathway Topology

	Using Gaussian graphical models we propose a novel approach to
             perform pathway analysis using gene expression. Given the
             structure of a graph (a pathway) we introduce two statistical
             tests to compare the mean and the concentration matrices between
             two groups. Specifically, these tests can be performed on the
             graph and on its connected components (cliques). The package is
             based on the method described in Massa M.S., Chiogna M., Romualdi
             C. (2010) <doi:10.1186/1752-0509-4-121>.
	"""
	
	cran = "topologyGSA" 

	version("1.5.0", md5="c570b23e5732db31fba8e8f93f2de1bb")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-grbase@2:", type=("build", "run"))
	depends_on("r-qpgraph", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
