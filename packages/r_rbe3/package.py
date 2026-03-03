# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbe3(RPackage):
	"""Estimation and Additional Tools for Quantile Generalized Beta
Regression Model

	Provide estimation and data generation tools for the quantile generalized beta 
        regression model. For details, see Bourguignon, Gallardo and Saulo <arXiv:2110.04428>
        The package also provides tools to perform covariates selection.
	"""
	
	cran = "RBE3" 

	version("1.1", md5="90b8cd0849f5f9e536188749650c199d", url="https://cran.r-project.org/src/contrib/RBE3_1.1.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
