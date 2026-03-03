# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmselect(RPackage):
	"""Gaussian Graphs Models Selection

	Graph estimation in Gaussian Graphical Models, following the method
  developed by C. Giraud, S. Huet and N. Verzelen (2012) <doi:10.1515/1544-6115.1625>.
  The main functions return the adjacency matrix of an undirected graph
  estimated from a data matrix.
	"""
	
	cran = "GGMselect" 

	version("0.1-12.7", md5="36ed03bc6152bba8af4cd145ae2a085d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
