# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMboost(RPackage):
	"""Model-Based Boosting

	Functional gradient descent algorithm
  (boosting) for optimizing general risk functions utilizing
  component-wise (penalised) least squares estimates or regression
  trees as base-learners for fitting generalized linear, additive
  and interaction models to potentially high-dimensional data.
  Models and algorithms are described in <doi:10.1214/07-STS242>,
  a hands-on tutorial is available from <doi:10.1007/s00180-012-0382-5>.
  The package allows user-specified loss functions and base-learners.
	"""
	
	homepage = "https://github.com/boost-R/mboost"
	cran = "mboost" 

	version("2.9-9", md5="d3e6df0653f9bd5fd1e9a5685bd8b663")

	# Fix build with R >= 4.5 (Calloc/Free macros moved)
	# Use filter_file instead of an external patch to be resilient to minor context changes
	def patch(self):
		if self.spec.satisfies("^r@4.5:"):
			filter_file(
				"#include <R_ext/BLAS.h> /* for dgemm */",
				"#include <R_ext/BLAS.h> /* for dgemm */\n"
				"#include <R_ext/RS.h>\n"
				"#include <R_ext/Memory.h>\n\n"
				"#ifndef Calloc\n"
				"#define Calloc(n, t) (t *) R_alloc((n), sizeof(t))\n"
				"#endif\n"
				"#ifndef Free\n"
				"#define Free(p) ((void)0)\n"
				"#endif\n",
				"src/mboost.c",
				string=True,
			)

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stabs@0.5.0:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival@3.2.10:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-partykit@1.2.1:", type=("build", "run"))
