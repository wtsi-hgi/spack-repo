# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoismf(RPackage):
	"""Factorization of Sparse Counts Matrices Through Poisson
Likelihood

	Creates a non-negative low-rank approximate factorization of a sparse counts matrix by maximizing Poisson
    likelihood with L1/L2 regularization (e.g. for implicit-feedback recommender systems or bag-of-words-based topic modeling)
    (Cortes, (2018) <arXiv:1811.01908>), which usually leads to very sparse user and item factors (over 90% zero-valued).
    Similar to hierarchical Poisson factorization (HPF), but follows an optimization-based approach with regularization
    instead of a hierarchical prior, and is fit through gradient-based methods instead of variational inference.
	"""
	
	homepage = "https://github.com/david-cortes/poismf"
	cran = "poismf" 

	version("0.4.0-4", md5="d6c85b6525e146d06460721cef0006cd")

	depends_on("r-matrix@1.3:", type=("build", "run"))
