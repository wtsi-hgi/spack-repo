# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSglasso(RPackage):
	"""Lasso Method for RCON(V,E) Models

	RCON(V, E) models are a kind of restriction of the Gaussian Graphical Models defined by a set of equality constraints on the entries of the concentration matrix. 'sglasso' package implements the structured graphical lasso (sglasso) estimator proposed in Abbruzzo et al. (2014) for the weighted l1-penalized RCON(V, E) model. Two cyclic coordinate algorithms are implemented to compute the sglasso estimator, i.e. a cyclic coordinate minimization (CCM) and a cyclic coordinate descent (CCD) algorithm.
	"""
	
	homepage = "http://www.unipa.it/persone/docenti/a/luigi.augugliaro"
	cran = "sglasso" 

	version("1.2.6", md5="d00804f707e4502b389076d89e23e912")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r@4.2:", type=("build", "run"))
