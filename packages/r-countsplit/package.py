# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountsplit(RPackage):
	"""Splitting a Count Matrix into Independent Folds

	Implements the count splitting methodology from Neufeld et al. (2022) <doi:10.1093/biostatistics/kxac047> and Neufeld et al. (2023) <arXiv:2307.12985>. Intended for turning a matrix of single-cell RNA sequencing counts, or similar count datasets, into independent folds that can be used for training/testing or cross validation. Assumes that the entries in the matrix are from a Poisson or a negative binomial distribution.
	"""
	
	homepage = "https://github.com/anna-neufeld/countsplit"
	cran = "countsplit" 

	version("4.0.0", md5="86c684b6377ab25d96e0f30d7a4b942b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
