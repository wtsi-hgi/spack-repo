# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvs(RPackage):
	"""Tools for Semantic Vector Spaces

	Various tools for semantic vector spaces, such as
    correspondence analysis (simple, multiple and discriminant), latent
    semantic analysis, probabilistic latent semantic analysis, non-negative
    matrix factorization, latent class analysis, EM clustering, logratio
	analysis and log-multiplicative (association) analysis. Furthermore,
    there are specialized distance measures, plotting functions and some helper
    functions.
	"""
	
	cran = "svs" 

	version("3.0.0", md5="96d947d405957f854286b2622db8ef34")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
