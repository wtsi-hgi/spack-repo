# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvtree(RPackage):
	"""Evolutionary Learning of Globally Optimal Trees

	Commonly used classification and regression tree methods like the CART algorithm
             are recursive partitioning methods that build the model in a forward stepwise search.
	     Although this approach is known to be an efficient heuristic, the results of recursive
	     tree methods are only locally optimal, as splits are chosen to maximize homogeneity at
	     the next step only. An alternative way to search over the parameter space of trees is
	     to use global optimization methods like evolutionary algorithms. The 'evtree' package
	     implements an evolutionary algorithm for learning globally optimal classification and
	     regression trees in R. CPU and memory-intensive tasks are fully computed in C++ while
	     the 'partykit' package is leveraged to represent the resulting trees in R, providing
	     unified infrastructure for summaries, visualizations, and predictions.
	"""
	
	cran = "evtree" 

	version("1.0-8", md5="52b5bf9c1e770437a0419407870eac2f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
