# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmf(RPackage):
	"""Collective Matrix Factorization

	Collective matrix factorization (CMF) finds joint low-rank
	representations for a collection of matrices with shared row or column
	entities. This code learns a variational Bayesian approximation for CMF,
	supporting multiple likelihood potentials and missing data, while
	identifying both factors shared by multiple matrices and factors private
	for each matrix. For further details on the method see
	Klami et al. (2014) <arXiv:1312.5921>.
	The package can also be used to learn Bayesian canonical correlation
	analysis (CCA) and group factor analysis (GFA) models, both of which are
	special cases of CMF. This is likely to be useful for people looking for
	CCA and GFA solutions supporting missing data and non-Gaussian likelihoods.
	See Klami et al. (2013) <https://research.cs.aalto.fi/pml/online-papers/klami13a.pdf>
	and	Virtanen et al. (2012) <http://proceedings.mlr.press/v22/virtanen12.html>
	for details on Bayesian CCA and GFA, respectively.
	"""
	
	cran = "CMF" 

	version("1.0.3", md5="9d297e6157af120213cd5db86e3230e1")

	depends_on("r-cpp11", type=("build", "run"))
