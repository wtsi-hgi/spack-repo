# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcsteiner(RPackage):
	"""Convenient Tool for Solving the Prize-Collecting Steiner Tree
Problem

	The Prize-Collecting Steiner Tree problem asks to find a subgraph
    connecting a given set of vertices with the most expensive nodes and least
    expensive edges. Since it is proven to be NP-hard, exact and efficient algorithm
    does not exist. This package provides convenient functionality for obtaining an
    approximate solution to this problem using loopy belief propagation algorithm.
	"""
	
	homepage = "https://github.com/krashkov/pcSteiner"
	cran = "pcSteiner" 

	version("1.0.0.1", md5="5e4a8c18a34287942e32298afe44e51c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-igraph@0.6:", type=("build", "run"))
