# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcplex(RPackage):
	"""R Interface to CPLEX

	R interface to CPLEX solvers for linear, quadratic, and (linear and quadratic) mixed integer programs. Support for quadratically constrained programming is available. See the file "INSTALL" for details on how to install the Rcplex package in Linux/Unix-like and Windows systems. Support for sparse matrices is provided by an S3-style class "simple_triplet_matrix" from package slam and by objects from the Matrix package class hierarchy.
	"""
	
	homepage = "https://R-Forge.R-project.org/projects/rcplex"
	cran = "Rcplex" 

	version("0.3-6", md5="841354f4982e05fccfc5adfbb1a83eab")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("cplex", type=("build", "link", "run"))
