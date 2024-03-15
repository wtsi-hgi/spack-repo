# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimdag(RPackage):
	"""Simulate Data from a DAG and Associated Node Information

	Simulate complex data from a given directed acyclic graph and information about each individual node.
	Root nodes are simply sampled from the specified distribution. Child Nodes are simulated according to
	one of many implemented regressions, such as logistic regression, linear
	regression, poisson regression and more. Also includes a comprehensive framework for discrete-time
	simulation, which can generate even more complex longitudinal data.
	"""
	
	homepage = "https://github.com/RobinDenz1/simDAG"
	cran = "simDAG" 

	version("0.1.1", md5="2a25dd7904c2c703fc9378b4781a2b63")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
