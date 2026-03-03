# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestedcategbayesimpute(RPackage):
	"""Modeling, Imputing and Generating Synthetic Versions of Nested
Categorical Data in the Presence of Impossible Combinations

	This tool set provides a set of functions to fit the nested Dirichlet process mixture of products of multinomial distributions (NDPMPM) model for nested categorical household data in the presence of impossible combinations. It has direct applications in imputing missing values for and generating synthetic versions of nested household data.
	"""
	
	cran = "NestedCategBayesImpute" 

	version("1.2.1", md5="5fbc2e9c02bed668c711c8d08ea66af9")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
